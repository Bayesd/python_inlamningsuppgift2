
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

def operation(selected):
    if selected == 1:
        return add
    elif selected == 2:
        return subtract
    elif selected == 3:
        return multiply
    elif selected == 4:
        return divide
    else:
        return modulo

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, Y):
    return x % y

first_number = int(input("Enter first number: "))
select_operation = int(input("What operation? \nPress 1 for +\nPress 2 for -\nPress 3 for *\nPress 4 for/\n"))
second_number = int(input("Enter second number: "))