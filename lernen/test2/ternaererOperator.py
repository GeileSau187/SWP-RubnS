def main():
    a=18
    b = "minderjährig" if a <= 18 else "volljährig"
    print(b)

    c = [10, 29, 30, 1, 23, 4]
    d = ["minderjährig" if i <= 18 else "volljährig" for i in c]
    print(d)

if __name__ == "__main__":
    main()