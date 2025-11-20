from typing import List, Dict

class Extractor:
    def extract(self, tokens: List[str]) -> List[Dict]:
        if not tokens: return []
        return [{"ozne": tokens[0], "eylem": tokens[1] if len(tokens) > 1 else "", "nesne": " ".join(tokens[2:])}]
