def arithmetic_arranger(problems, show_answers=False):
    char_top = []
    char_bottom = []
    line = []
    answer = []

    if len(problems) > 5:
        return 'Error: we do not accept more than 5 problems'

    for problem in problems:
        char = problem.split()
        arg1 = char[0]
        operator = char[1]
        arg2 = char[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be either '+' or '-'"
        if not arg1.isdigit() or not arg2.isdigit():
            return 'Error: Numbers must only contain digits'
        if len(arg1) > 4 or len(arg2) > 4:
            return 'Error: Numbers cannot be more than four digits'

        max_length = max(len(arg1), len(arg2)) + 2

        char_top.append(arg1.rjust(max_length))
        char_bottom.append(operator + arg2.rjust(max_length - 1))
        line.append("-" * max_length)

        if show_answers:
            if operator == '+':
                result = str(int(arg1) + int(arg2))
            else:
                result = str(int(arg1) - int(arg2))
            answer.append(result.rjust(max_length))

    arrangement = ""
    if char_top:
        arrangement += "    ".join(char_top) + "\n"
    if char_bottom:
        arrangement += "    ".join(char_bottom) + "\n"
    if line:
        arrangement += "    ".join(line) + "\n"
    if show_answers and answer:
        arrangement += "    ".join(answer)

    return arrangement.rstrip()

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
