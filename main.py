def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        return None

def get_number(prompt):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operation = input("Select operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
            if result is None:
                continue

        print(f"{num1} {operation} {num2} = {result}")

        choice = input("Would you like to do a new calculation? (yes/no) ")
        if choice.lower() == 'no':
            break

if __name__ == "__main__":
    main()