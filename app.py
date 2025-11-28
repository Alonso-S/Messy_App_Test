# messy_app/app.py
import sys
from utils.string_utils import clean_text, count_words
from utils.file_utils import read_file, write_file
from core.processor import process_data
from core.analyzer import analyze_data
from security.insecure_ops import insecure_hash_password

# Spaghetti global state
GLOBAL_CACHE = {}

def main():
    if len(sys.argv) < 2:
        print("No input file provided")
        return

    filename = sys.argv[1]

    # Horrible chaining and repeated logic
    try:
        content = read_file(filename)
        cleaned = clean_text(content)

        if filename not in GLOBAL_CACHE:
            GLOBAL_CACHE[filename] = cleaned

        for i in range(3):
            result = process_data(cleaned)
            print("Iteration", i, "->", result)

        analysis = analyze_data(cleaned)
        print("Analysis:", analysis)

        # INSECURE OPERATION
        pwd = insecure_hash_password("admin123")
        print("Insecure hash:", pwd)

        write_file(filename + ".out", cleaned)

    except:
        # Silent error (Security smell + bad practice)
        pass

if __name__ == "__main__":
    main()
