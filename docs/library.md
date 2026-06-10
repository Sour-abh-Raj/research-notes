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
    P5["📄 Mayer, Davis & Schoorman (1995)<br/>ABI Model of Trust"]
    P6["📄 Lee & See (2004)<br/>Trust Calibration"]
    P7["📄 McKnight et al. (1998)<br/>Institution-based Trust"]
    A1["📝 Understanding Literature Reviews"]
    A2["📝 Bibliometric & Thematic Analysis Field Manual"]
    A3["📝 When Trust Becomes Epistemic"]
    T1(["Research methods"])
    T2(["Literature reviews"])
    T3(["Science mapping"])
    T4(["Topic modeling"])
    T5(["Trust in AI"])
    T6(["Epistemic trust"])

    P1 --> A1
    P2 --> A2
    P3 --> A2
    P4 --> A2
    P5 --> A3
    P6 --> A3
    P7 --> A3
    A1 --- T1
    A1 --- T2
    A2 --- T1
    A2 --- T3
    A2 --- T4
    A3 --- T5
    A3 --- T6

    classDef paper fill:#e8eaf6,stroke:#3f51b5,color:#1a237e;
    classDef article fill:#e0f2f1,stroke:#00897b,color:#004d40;
    classDef topic fill:#fff,stroke:#9e9e9e,color:#424242,stroke-dasharray: 4 3;
    class P1,P2,P3,P4,P5,P6,P7 paper;
    class A1,A2,A3 article;
    class T1,T2,T3,T4,T5,T6 topic;
```

## Papers read

| Paper | Area | Article | Read |
|-------|------|---------|------|
| Siddaway, A. P., Wood, A. M., & Hedges, L. V. (2019). *How to Do a Systematic Review: A Best Practice Guide for Conducting and Reporting Narrative Reviews, Meta-Analyses, and Meta-Syntheses.* Annual Review of Psychology, 70, 747–770. [doi](https://doi.org/10.1146/annurev-psych-010418-102803) | Research methods · Literature reviews | [Understanding Literature Reviews](blog/posts/understanding-literature-reviews.md) | Jun 2026 |
| Paré, G., Trudel, M.-C., Jaana, M., & Kitsiou, S. (2015). *Synthesizing information systems knowledge: A typology of literature reviews.* Information & Management, 52(2), 183–199. [doi](https://doi.org/10.1016/j.im.2014.08.008) | Research methods · Review typology | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Grootendorst, M. (2022). *BERTopic: Neural topic modeling with a class-based TF-IDF procedure.* arXiv:2203.05794. [arxiv](https://arxiv.org/abs/2203.05794) | Topic modeling · Thematic analysis | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Traag, V. A., Waltman, L., & van Eck, N. J. (2019). *From Louvain to Leiden: guaranteeing well-connected communities.* Scientific Reports, 9, 5233. [doi](https://doi.org/10.1038/s41598-019-41695-z) | Network science · Community detection | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Zupic, I., & Čater, T. (2015). *Bibliometric methods in management and organization.* Organizational Research Methods, 18(3), 429–472. [doi](https://doi.org/10.1177/1094428114562629) | Research methods · Science mapping | [Bibliometric & Thematic Analysis Field Manual](blog/posts/bibliometric-analysis-field-manual.md) | Jun 2026 |
| Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). *An integrative model of organizational trust.* Academy of Management Review, 20(3), 709–734. [doi](https://doi.org/10.2307/258792) | Trust theory · Organizational trust | [When Trust Becomes Epistemic](blog/posts/epistemic-trust-generative-ai-gap.md) | Jun 2026 |
| Lee, J. D., & See, K. A. (2004). *Trust in automation: Designing for appropriate reliance.* Human Factors, 46(1), 50–80. [doi](https://doi.org/10.1518/hfes.46.1.50_30392) | Trust calibration · Human-automation | [When Trust Becomes Epistemic](blog/posts/epistemic-trust-generative-ai-gap.md) | Jun 2026 |
| McKnight, D. H., Cummings, L. L., & Chervany, N. L. (1998). *Initial trust formation in new organizational relationships.* Academy of Management Review, 23(3), 473–490. [doi](https://doi.org/10.2307/259290) | Trust theory · Institution-based trust | [When Trust Becomes Epistemic](blog/posts/epistemic-trust-generative-ai-gap.md) | Jun 2026 |
| Sperber, D., et al. (2010). *Epistemic vigilance.* Mind & Language, 25(4), 359–393. [doi](https://doi.org/10.1111/j.1468-0017.2010.01394.x) | Epistemic trust · Testimony | [When Trust Becomes Epistemic](blog/posts/epistemic-trust-generative-ai-gap.md) | Jun 2026 |

!!! tip "How to read this page"
    A paper can map to more than one article over time, and an article can draw on more than one
    paper. As the knowledge base grows, this table and the graph above become a map of how the ideas
    in my research — **AI adoption**, **trust in AI**, and the **organizational context** of
    technology use — fit together.
