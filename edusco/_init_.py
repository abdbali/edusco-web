from .core import Edusco
from .models import EduscoModel
from .spelling import SpellingCorrector
from .tokenizer import Tokenizer
from .parser import POSParser
from .morphology import MorphologyAnalyzer
from .ontology import OntologyMatcher
from .extractor import Extractor
from .pronoun_resolver import PronounResolver

__all__ = [
    "Edusco",
    "EduscoModel",
    "SpellingCorrector",
    "Tokenizer",
    "POSParser",
    "MorphologyAnalyzer",
    "OntologyMatcher",
    "Extractor",
    "PronounResolver"
]
