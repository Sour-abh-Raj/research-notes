from __future__ import annotations

import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
MKDOCS = ROOT / "mkdocs.yml"


@dataclass(frozen=True)
class Post:
    title: str
    date: str
    slug: str
    categories: tuple[str, ...]


def fail(message: str) -> None:
    print(f"verify_site: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing expected file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def front_matter(markdown: str) -> tuple[dict[str, object], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown

    try:
        _, raw, body = markdown.split("---\n", 2)
    except ValueError:
        fail("unterminated front matter block")

    data: dict[str, object] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            value = line[4:].strip().strip("'\"")
            assert isinstance(data[current_key], list)
            data[current_key].append(value)
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip()
            if value:
                data[current_key] = value.strip("'\"")
            else:
                data[current_key] = []

    return data, body


def page_title(body: str, path: Path) -> str:
    match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    if not match:
        fail(f"missing H1 title in {path.relative_to(ROOT)}")
    return match.group(1).strip()


def slugify_category(category: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")


def load_posts() -> list[Post]:
    posts: list[Post] = []
    for path in sorted((DOCS / "blog" / "posts").glob("*.md")):
        data, body = front_matter(read(path))
        missing = [key for key in ("date", "slug", "categories") if not data.get(key)]
        if missing:
            fail(f"{path.relative_to(ROOT)} missing front matter: {', '.join(missing)}")

        categories = data["categories"]
        if not isinstance(categories, list):
            fail(f"{path.relative_to(ROOT)} categories must be a YAML list")

        posts.append(
            Post(
                title=page_title(body, path),
                date=str(data["date"]),
                slug=str(data["slug"]),
                categories=tuple(str(category) for category in categories),
            )
        )
    return posts


def assert_contains(path: Path, *needles: str) -> str:
    text = read(path)
    for needle in needles:
        if html.escape(needle, quote=False) not in text and needle not in text:
            fail(f"{path.relative_to(ROOT)} does not contain: {needle}")
    return text


def verify_blog(posts: list[Post]) -> None:
    if not posts:
        fail("no blog posts found")

    blog_index = SITE / "blog" / "index.html"
    sorted_posts = sorted(posts, key=lambda post: post.date, reverse=True)
    assert_contains(blog_index, sorted_posts[0].title)

    for post in posts:
        year, month, day = post.date.split("-")
        rendered = SITE / "blog" / year / month / day / post.slug / "index.html"
        assert_contains(rendered, post.title)
        assert_contains(blog_index, post.title)

        for category in post.categories:
            category_page = SITE / "blog" / "category" / slugify_category(category) / "index.html"
            assert_contains(category_page, category, post.title)


def verify_thoughts() -> None:
    thoughts_index = SITE / "thoughts" / "index.html"
    thought_paths = sorted((DOCS / "thoughts").glob("thought-*.md"))
    if not thought_paths:
        fail("no thought pages found")

    for path in thought_paths:
        title = page_title(front_matter(read(path))[1], path)
        slug = path.stem
        assert_contains(SITE / "thoughts" / slug / "index.html", title)
        assert_contains(thoughts_index, slug)


def verify_meta() -> None:
    config = read(MKDOCS)
    site_name_match = re.search(r"^site_name:\s*(.+)$", config, flags=re.MULTILINE)
    description_match = re.search(r"^site_description:\s*(.+)$", config, flags=re.MULTILINE)
    if not site_name_match or not description_match:
        fail("mkdocs.yml must define site_name and site_description")

    site_name = site_name_match.group(1).strip().strip("'\"")
    site_description = description_match.group(1).strip().strip("'\"")
    home = assert_contains(SITE / "index.html", site_name)
    if site_description not in home and html.escape(site_description, quote=True) not in home:
        fail("site/index.html does not contain the configured site_description")


def main() -> None:
    posts = load_posts()
    verify_blog(posts)
    verify_thoughts()
    verify_meta()
    print("verify_site: rendered blog posts, categories, thoughts, and meta look good")


if __name__ == "__main__":
    main()
