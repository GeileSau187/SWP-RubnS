#dictionary


def create_dicionary():
    alphabet_dict = {chr(97 + i): i + 1 for i in range(26)}
    return alphabet_dict

def mainDict():
    alphabet = create_dicionary()
    print(alphabet)

if __name__ == "__main__":
    mainDict()