
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
        return +
    elif selected == 2:
        return -
    elif selected == 3:
        return *
    elif selected == 4:
        return /
    else:
        return %

first_number = int(input("Enter first number: "))
select_operation = int(input("What operation? /nPress 1 for +/nPress 2 for -/n Press 3 for */Press 4 for /"))
second_number = int(input("Enter second number: "))