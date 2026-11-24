"""Independent synthetic evidence graph example; no external requests."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Link:
    claim: str
    source: str
    relation: str

def summarize(claim: str, links: list[Link]) -> dict:
    if not claim.strip():
        raise ValueError("Claim identifier required")
    result = {"supports": [], "contradicts": [], "uncertain": []}
    seen = set()
    for link in links:
        if link.relation not in result or not link.source.strip():
            raise ValueError("Invalid evidence link")
        key = (link.claim, link.source, link.relation)
        if link.claim == claim and key not in seen:
            result[link.relation].append(link.source)
            seen.add(key)
    return result

if __name__ == "__main__":
    print(summarize("fictional-claim", [Link("fictional-claim", "synthetic-A", "supports"), Link("fictional-claim", "synthetic-B", "contradicts")]))
