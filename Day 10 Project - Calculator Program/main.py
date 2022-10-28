from art import logo


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
    print(logo)
    first_num = float(input("What's the first number: "))
    for operation in operations:
        print(operation)
    is_on = True
    while is_on:
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number: "))
        calculation = operations[operation]
        answer = calculation(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")
        other_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation, or 'off' to exit: ").lower()
        if other_operation == "y":
            first_num = answer
        elif other_operation == "n":
            calculator()
        else:
            is_on = False


calculator()
