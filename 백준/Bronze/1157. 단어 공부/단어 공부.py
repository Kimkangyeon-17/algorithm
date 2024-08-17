from collections import Counter

def most_common(w):
    w = w.upper()
    counter = Counter(w)
    max_count = max(counter.values())

    most_common_letter = [letter for letter, count in counter.items() if count == max_count]

    if len(most_common_letter) > 1:
        return "?"
    else:
        return most_common_letter[0]

w = input()

print(most_common(w))