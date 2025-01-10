import os
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    keep_going = False
    os.system('cls')
    print(art.logo)
    first_number = float(input("Enter first number: "))
    while not keep_going:
        for i in operations:
            print(i)
        operation = input("Chose an operation:")
        second_number = float(input("Enter second number: "))
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        print(f"Do you want to continue making operations with {result}? OR start a new calculation?")
        choice = input(f"Type 'y' or 'n' or 'exit to exit the program: ")
        if choice == 'n':
            keep_going = True
            calculator()
        elif choice == 'exit':
            break
        else:
            first_number = result
            os.system('cls')


calculator()

