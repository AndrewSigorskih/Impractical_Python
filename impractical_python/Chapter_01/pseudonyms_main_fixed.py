import sys
import random
import json
from os import path
from typing import Generator


def gen_pseudonyms() -> Generator[str, None, None]:
    data_pth = path.join(path.dirname(__file__), 'pseudonyms.json')
    with open(data_pth, 'r') as f:
        dct = json.load(f)
    while True:
        first_name = random.choice(dct["first"])
        last_name = random.choice(dct["last"])
        yield f"{first_name} {last_name}"


def main():
    print("Welcome to the Psych 'Sidekick Name Picker'.\n")
    print("A name just like Sean would pick for Gus:\n\n")
    gen = gen_pseudonyms()
    while True:
        print("\n\n")
        print(next(gen), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break
    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
