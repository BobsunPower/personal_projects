# First working solution
# Tested in PyCharm using personal laptop because of lack of administration rights to install software.
# It doesn't recognise negative numbers.
operators = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y)
}


def rpn_calculator(data):
    basic_math_operators = ["+", "-", "*", "/"]
    stack_of_nums = []
    list_of_operators = []
    for ch in data.split():
        if ch.isdigit():
            stack_of_nums.append(float(ch))
        elif ch in basic_math_operators:
            list_of_operators.append(ch)
        else:
            print("Invalid input data")
            exit()
    result = stack_of_nums.pop()
    while stack_of_nums and list_of_operators:
        current = result
        result = operators[list_of_operators.pop(0)](current, stack_of_nums.pop())
    print(int(result))


rpn_calculator(input())
