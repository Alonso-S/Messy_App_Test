# messy_app/utils/string_utils.py
import re

def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text

def remove_special(text):
    # Dead code and duplication
    text = text.lower().strip()
    return re.sub(r"[^a-zA-Z0-9 ]", "", text)

def count_words(text):
    # Overly complicated counting
    words = []
    for w in text.split(" "):
        if len(w) > 0:
            words.append(w)
    return len(words)
