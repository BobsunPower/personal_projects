# Completed solution.
operators = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y)
}


def rpn_calculator(data):
    stack_of_nums = []
    list_of_operators = []
    for ch in data.split():
        # Check if the character is negative number.
        if len(ch) == 2:
            stack_of_nums.append(float(ch))
            continue
        # Check if the character is positive number.
        if ch.isdigit():
            stack_of_nums.append(float(ch))
        # Check if the character operator.
        elif ch in operators:
            list_of_operators.append(ch)
        # In case of invalid input it returns error.
        else:
            print("Error: Invalid input.")
            exit()
    result = stack_of_nums.pop()
    while stack_of_nums and list_of_operators:
        current = result
        result = operators[list_of_operators.pop(0)](current, stack_of_nums.pop())
    print(int(result))


rpn_calculator(input())
