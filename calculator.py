def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            # Get user input for operation
            choice = input("Enter choice (1/2/3/4): ")

            # Check if the choice is one of the four options
            if choice in ['1', '2', '3', '4']:
                # Get user input for numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")

                # Ask if the user wants to perform another calculation
                next_calculation = input(
                    "Do you want to perform another calculation? (yes/no): ").lower()
                if next_calculation != 'yes':
                    print("Thanks for using the calculator!")
                    break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input. Please enter a number.")


if __name__ == "__main__":
    main()
