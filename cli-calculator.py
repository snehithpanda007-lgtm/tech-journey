def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return a / b


def get_numbers():
    try:
        num1 = float(input("Enter first value: "))
        num2 = float(input("Enter second value: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Enter numeric values.")
        return None, None


def main():
    print("CLI Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1-4): "))
    except ValueError:
        print("Invalid choice")
        return

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice")
        return

    num1, num2 = get_numbers()
    if num1 is None:
        return

    try:
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = sub(num1, num2)
        elif choice == 3:
            result = mul(num1, num2)
        elif choice == 4:
            result = div(num1, num2)

        print(f"Result = {result}")

    except ZeroDivisionError as error:
        print(error)


if __name__ == "__main__":
    main()