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

def calculate(first_number, operation, second_number):
    if operation == 1:
        return first_number + second_number
    elif operation == 2:
        return first_number - second_number
    elif operation == 3:
        return first_number * second_number
    elif operation == 4:
        return first_number / second_number
    else:
        return first_number % second_number5

first_number = int(input("Enter first number: "))
operation = int(input("What operation? \nPress 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\n"))
second_number = int(input("Enter second number: "))
print(print_result(calculate(first_number, operation, second_number)))