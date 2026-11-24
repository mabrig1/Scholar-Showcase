import unittest
from evidence import Link, summarize

class EvidenceTests(unittest.TestCase):
    def test_mixed_evidence_and_deduplication(self):
        a = Link("C", "A", "supports")
        self.assertEqual(summarize("C", [a, a, Link("C", "B", "contradicts"), Link("other", "X", "supports")]), {"supports":["A"], "contradicts":["B"], "uncertain":[]})
    def test_unknown_relation_rejected(self):
        with self.assertRaises(ValueError):
            summarize("C", [Link("C", "A", "proves")])
    def test_empty_evidence(self):
        self.assertEqual(summarize("C", []), {"supports":[], "contradicts":[], "uncertain":[]})

if __name__ == "__main__":
    unittest.main()
