# messy_app/core/processor.py
def process_data(text):
    total = 0
    for word in text.split(" "):
        if len(word) > 3:
            total += 1
        else:
            if len(word) == 3:
                total += 0.5
            else:
                if len(word) == 2:
                    total += 0.25
                else:
                    if len(word) == 1:
                        total += 0.1
    if total > 10:
        total = total / 2
    else:
        if total > 5:
            total = total - 1
        else:
            if total > 2:
                total = total + 3
            else:
                total = total * 2
    return total
