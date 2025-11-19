start_number = 1
end_number = 20
def create_list():
    numbers = list(range(start_number, end_number + 1))
    labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
    return numbers, labels

def main():
    print(create_list())

if __name__ == "__main__":
    main()