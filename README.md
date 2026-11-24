# MABRIG Scholar | Research Engineering Portfolio

**Scholarly infrastructure · Evidence intelligence · Responsible AI research systems**

[Product website](https://scholar.mabrigkorie.org) · [Developer profile](https://github.com/mabrig1) · [Contact](https://www.mabrigkorie.org)

Scholar (Researcher Pro) brings together research assistance, scholarly publishing workflows, manuscript screening and moderated scholarly deposits. The original documentation describes Crossref and OpenAlex discovery and research integrity safeguards. This public portfolio illustrates engineering concepts without exposing private implementation details or claiming independent verification of production functionality.

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive synthetic evidence graph](demo/index.html) — download and open locally in a browser.
- [Independent evidence relationship example](demo/evidence.py)
- [Automated tests](demo/test_evidence.py)
- [CI workflow](.github/workflows/demo.yml)

## Demonstrated engineering competencies

Evidence provenance, scholarly metadata, graph relationships, input validation, human-review boundaries, reproducible examples and responsible research data management.

## Run locally

```sh
python demo/evidence.py
python -m unittest discover -s demo -v
```

Python 3.10+; no external dependencies or API keys. All sample evidence is fictional. The demonstrations do not establish scientific truth, validate real DOI records, guarantee journal acceptance or guarantee academic indexing. Evidence Atlas is presented as a design concept, not a claim of completed deployment.

## Intellectual property and collaboration

See [NOTICE.md](NOTICE.md). Production source, unpublished manuscripts, private research data and credentials are excluded. Public scholarly works retain their applicable individual licences. Recruiters and research collaborators may contact MABRIG Technologies for a guided demonstration or scoped technical review.
