import this

def to_int(input_from_user):
    try:
        return int(input_from_user)
    except Exception:
        print("Error!")


def print_result(result):
    if result < 50:
        return("Less then fifty")
    elif result == 50:
        return("Fifty")
    elif result > 50 and result < 100:
        return("Almost a hundred")
    elif result == 100:
        return("Spot on!")
    elif result > 100:
        return("Missed the spot!")
    else:
        return("Something went wrong")

def calculate(first_number, second_number, operation):
    try:
        if operation == "+":
            return first_number + second_number
        elif operation == "-":
            return first_number - second_number
        elif operation == "*":
            return first_number * second_number
        elif operation == "/":
            return first_number / second_number
        else:
            return first_number % second_number5
    except Exception:
        print("Could not recognize the operator")


first_number = to_int(input("Enter first number: "))
operation = input("Select +, -, * or /\n")
second_number = to_int(input("Enter second number: "))
print(print_result(calculate(first_number, second_number, operation)))
