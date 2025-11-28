# messy_app/core/analyzer.py
from utils.string_utils import clean_text
from core.processor import process_data

# Circular dependency when used by other modules in tests or expansions

def analyze_data(text):
    scores = []
    cleaned = clean_text(text)

    for i in range(len(cleaned)):
        piece = cleaned[:i]
        score = process_data(piece)
        scores.append(score)

    return {
        "max": max(scores),
        "min": min(scores),
        "avg": sum(scores) / len(scores),
        "items": scores
    }
