from typing import List, Dict

class POSParser:
    def parse(self, tokens: List[str]) -> List[Dict]:
        return [{"token": t, "pos": "NOUN"} for t in tokens]
