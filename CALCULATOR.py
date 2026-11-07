import math

def calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    choice = input("Enter the operation (+, -, *, /, **, EXIT): ")
    if choice == '+':
        print(num1 + num2)
    elif choice == '-':
        print(num1 - num2)
    elif choice == '/':
        print(num1 / num2)
    elif choice == '*':
        print(num1 * num2)
    elif choice == '**':
        print(num1 ** num2)
    elif choice == "EXIT":
        print("Exiting the calculator.")
calculate()
                        