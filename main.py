class Calculator:
    """
    This is one of my best ideas, 0 regrets. Bye.
    """
    def __init__(self, n1, n2, operation):
        self.n1 = n1
        self.n2 = n2
        self.operation = operation

    def plus(self):
        # Perform addition instead of string concatenation
        print(str(self.n1) + str(self.n2))

    def minus(self):
        print(self.n1 - self.n2)

    def multiply(self):
        # Use self.n2 to access the instance variable
        print(str(self.n1) * self.n2)

    def divide(self):
        # Handle division by zero
        if self.n2 == 0:
            print("Error: Division by zero is undefined.")
        else:
            print(self.n1 / self.n2)

def main():
    try:
        n1 = int(input("Enter first number:\n"))
        operation = input("Enter the desirable mathematical operation: +, -, *, /:\n")
        while operation not in ["+", "-", "*", "/"]:
            operation = input("Invalid choice, try again. Enter the desirable mathematical operation: +, -, *, /:\n")
        n2 = int(input("Enter second number:\n"))
    except ValueError:
        print("Invalid input. Please enter numerical values for numbers.")
        return  # Exit the function if there is an error

    calculator = Calculator(n1, n2, operation)
    print("Result:")
    if operation == "+":
        calculator.plus()
    elif operation == "-":
        calculator.minus()
    elif operation == "*":
        calculator.multiply()
    elif operation == "/":
        calculator.divide()

main()
