VOWELS = "aeiou"


def piglatinize(word: str) -> str:
    if word[0] in VOWELS:
        return word + "way"
    return word[1:] + word[0] + "ay"


def main():
    while True:
        word = input("Type a word to get its pig Latin translation: ")
        print("\n\n")
        print(piglatinize(word))
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
        if try_again.lower() == "n":
            break
    input("Press Enter to exit.")


if __name__ == "__main__":
    main()
