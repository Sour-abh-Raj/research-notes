---
description: >-
  The Library — a running map of every paper Sourabh Raj reads and the article(s)
  it connects to. A single repository and knowledge base for Information Systems
  research on AI adoption, trust in AI, and research methods.
---

# Library

This is the **knowledge base** — a running map of every paper I read and the article(s) I've written
about it. The blog holds the deep dives; this page keeps the *connections* visible, so a paper is
never an orphan and the reading trail stays navigable.

Each row links the **paper** (to its source) and the **article** (my write-up). Browse by theme on
the [Topics](tags.md) page.

## Reading map

The graph shows how papers connect to articles and to the themes that tie the knowledge base
together. It grows with every post.

```mermaid
graph LR
    P1["📄 Siddaway, Wood & Hedges (2019)<br/>How to Do a Systematic Review"]
    P2["📄 Paré et al. (2015)<br/>Typology of Literature Reviews"]
    P3["📄 Grootendorst (2022)<br/>BERTopic"]
    P4["📄 Traag, Waltman & van Eck (2019)<br/>From Louvain to Leiden"]
    A1["📝 Understanding Literature Reviews"]
    A2["📝 Bibliometric & Thematic Analysis Field Manual"]
    T1(["Research methods"])
    T2(["Literature reviews"])
    T3(["Science mapping"])
    T4(["Topic modeling"])

    P1 --> A1
    P2 --> A2
    P3 --> A2
    P4 --> A2
    A1 --- T1
    A1 --- T2
    A2 --- T1
    A2 --- T3
    A2 --- T4

    classDef paper fill:#e8eaf6,stroke:#3f51b5,color:#1a237e;
    classDef article fill:#e0f2f1,stroke:#00897b,color:#004d40;
    classDef topic fill:#fff,stroke:#9e9e9e,color:#424242,stroke-dasharray: 4 3;
    class P1,P2,P3,P4 paper;
    class A1,A2 article;
    class T1,T2,T3,T4 topic;
```

## Papers read

| Paper | Area | Article | Read |
|-------|------|---------|------|
| Siddaway, A. P., Wood, A. M., & Hedges, L. V. (2019). *How to Do a Systematic Review: A Best Practice Guide for Conducting and Reporting Narrative Reviews, Meta-Analyses, and Meta-Syntheses.* Annual Review of Psychology, 70, 747–770. [doi](https://doi.org/10.1146/annurev-psych-010418-102803) | Research methods · Literature reviews | [Understanding Literature Reviews](blog/posts/understanding-literature-reviews.md) | Jun 2026 |
| Paré, G., Trudel, M.-C., Jaana, M., & Kitsiou, S. (2015). *Synthesizing information systems knowledge: A typology of literature reviews.* Information & Management, 52(2), 183–199. [doi](https://doi.org/10.1016/j.im.2014.08.008) | Research methods · Review typology | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Grootendorst, M. (2022). *BERTopic: Neural topic modeling with a class-based TF-IDF procedure.* arXiv:2203.05794. [arxiv](https://arxiv.org/abs/2203.05794) | Topic modeling · Thematic analysis | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Traag, V. A., Waltman, L., & van Eck, N. J. (2019). *From Louvain to Leiden: guaranteeing well-connected communities.* Scientific Reports, 9, 5233. [doi](https://doi.org/10.1038/s41598-019-41695-z) | Network science · Community detection | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Zupic, I., & Čater, T. (2015). *Bibliometric methods in management and organization.* Organizational Research Methods, 18(3), 429–472. [doi](https://doi.org/10.1177/1094428114562629) | Research methods · Science mapping | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |

!!! tip "How to read this page"
    A paper can map to more than one article over time, and an article can draw on more than one
    paper. As the knowledge base grows, this table and the graph above become a map of how the ideas
    in my research — **AI adoption**, **trust in AI**, and the **organizational context** of
    technology use — fit together.
