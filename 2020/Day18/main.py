import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def evaluate_line(componets):
    value = int(componets[0])
    i = 1
    while i < len(componets):
        if componets[i] == "+":
            value += int(componets[i + 1])
            i += 2
        elif componets[i] == "*":
            value *= int(componets[i + 1])
            i += 2

    return value


def process_line(componets):
    line_to_eval = list()
    i = 0
    new_line = list()
    parens_to_find = 0
    while i < len(componets):
        if componets[i][0:2] == "((":
            k = i + 1
            new_line.append(componets[i][1:])
            parens_to_find += 2
            while True:
                if componets[k][-1] == ")" and parens_to_find != 1:
                    new_line.append(componets[k])
                    parens_to_find -= 1
                    k += 1
                elif componets[k][-1] == ")":
                    new_line.append(componets[k][:-1])
                    break
                elif componets[k][0] == "(":
                    parens_to_find += 1
                    new_line.append(componets[k])
                    k += 1
                else:
                    new_line.append(componets[k])
                    k += 1
            value = process_line(new_line)
            line_to_eval.append(str(value))
            new_line.clear()
            i = k + 1

        elif componets[i][0] == "(":
            k = i + 1
            new_line.append(componets[i][1:])
            parens_to_find += 1
            while True:
                if componets[k][-1] == ")":
                    parens_to_find -= 1
                    if parens_to_find == 0:
                        new_line.append(componets[k][:-1])
                        break
                    else:
                        new_line.append(componets[k])
                        k += 1
                elif componets[k][0] == "(":
                    parens_to_find += 1
                    new_line.append(componets[k])
                    k += 1
                else:
                    new_line.append(componets[k])
                    k += 1
            value = process_line(new_line)
            line_to_eval.append(str(value))
            i = k + 1
            new_line.clear()
        else:
            line_to_eval.append(componets[i])
            i += 1
    return evaluate_line(line_to_eval)


def part1():
    sum = 0
    for problem in problems:
        line = problem.split(" ")
        result = process_line(line)
        sum += result
        print(result)

    # print(process_line(problems[5].split(" ")))
    return


def part2():
    pass


a = AOC(18, test=True)
problems = a.read_lines()
part1()
