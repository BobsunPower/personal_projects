# First working solution
# Tested in PyCharm using personal laptop because of lack of administration rights to install software.
# It doesn't recognise negative numbers.
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
        for index, operator in enumerate(list_of_operators):
            if operator == "*":
                list_of_operators.pop(index)
                result *= stack_of_nums.pop()
        for index, operator in enumerate(list_of_operators):
            if operator == "/":
                list_of_operators.pop(index)
                result /= stack_of_nums.pop()
        for index, operator in enumerate(list_of_operators):
            if operator == "+":
                list_of_operators.pop(index)
                result += stack_of_nums.pop()
        for index, operator in enumerate(list_of_operators):
            if operator == "-":
                list_of_operators.pop(index)
                result -= stack_of_nums.pop()
    print(int(result))


rpn_calculator(input())
