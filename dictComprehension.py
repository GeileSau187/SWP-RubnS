def create_alphabet_dict():
    # Dictionary Comprehension
    alphabet_dict = {chr(97 + i): i + 1 for i in range(26)}
    return alphabet_dict

def main():
    alphabet = create_alphabet_dict()
    print("Alphabet-Dictionary (a=1, b=2, ...):")
    for letter, number in alphabet.items():
        print(f"{letter}: {number}")

if __name__ == "__main__":
    main()
