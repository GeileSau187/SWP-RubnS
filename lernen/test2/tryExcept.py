def ternaererOperator():
    a = 19
    b = "volljaehrig" if a >= 18 else "minderjährig"
    print(a, b)

def zeroDivision():
    a = 8 / 0
    print(a)

def main():
    zeroDivision()
    # ternaererOperator()


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Error")
    except ZeroDivisionError:
        print("Error Zero Division")
    else:
        print("OK")
    finally:
        print("Closing function")