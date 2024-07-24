# TASK 01  **** SIMPLE CALCULATOR **** CODSOFT ****

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            result = add(num1, num2)
            print(f"The result is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result is: {result}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()
