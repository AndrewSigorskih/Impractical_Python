import pprint
from string import ascii_lowercase as alphabet
from collections import defaultdict
from typing import DefaultDict


def etaoin(text: str) -> DefaultDict[str, list]:
    mapping = defaultdict(list)
    for char in text:
        char = char.lower()
        if char in alphabet:
            mapping[char].append(char)
    for char in alphabet:
        if char not in mapping:
            mapping.__missing__(char)
    return mapping


def main():
    print("This program plots bar chart of character frequencies in text")
    print("You may need to stretch console window if text wrapping occurs.\n")
    text = input("Please enter your text or press Enter to see example:\n")
    if not text:
        text = "Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same."
    print("\n\n")
    print(f"{text=}")
    pprint.pprint(etaoin(text), width=110)


if __name__ == "__main__":
    main()
