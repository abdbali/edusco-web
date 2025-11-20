from typing import List

class Tokenizer:
    def tokenize(self, text: str) -> List[str]:
        return text.strip().lower().replace(",", "").replace(".", "").split()
