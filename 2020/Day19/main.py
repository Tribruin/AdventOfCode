import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

rules = dict()
messages = list()
solved_rules = list()


def parse_input(input):
    global rules
    global messages

    i = 0
    while input[i] != "":
        rule_num, rule_list = input[i].split(": ")
        y = [x.strip().strip('"') for x in rule_list.split("|")]
        new_rule = []
        for k in y:
            rule = [x if x in ["a", "b"] else int(x) for x in k.split(" ")]
            new_rule.append(rule)

        rules[int(rule_num)] = new_rule
        i += 1

    i += 1
    while i < len(input):
        messages.append(input[i])
        i += 1

    pass


def process_rule(rule):
    global rules
    rule_return = list()

    for rule_no, rule_variant in enumerate(rules[rule]):
        rule_varient_return = list()
        for item_no, item in enumerate(rule_variant):
            if type(item) is not int:
                # rules[rule][rule_no] == str(rules[item])
                # rules[rule_variant][item_no] = list(str(rules[item]))
                return item
            else:
                rule_varient_return += process_rule(item)
                rules[rule] = rule_return

            rule_return.append(rule_varient_return)
        # rules[rule][rule_no] = list(rule_varient_return)


def part1():
    global rules
    global message

    print(process_rule(0))

    # solved_rules = dict()
    # while len(rules) > 0:
    #     for rule_no, rule in rules.items():
    #         if rule_no not in solved_rules.keys():
    #             #TODO: PROCESS RULE
    #             for sub_rule in rule:
    #                 for sub_sub_rule in sub_rule:
    #                     if type(sub_sub_rule) = int:


def part2():
    pass


a = AOC(19, test=True)
input = a.read_lines()
parse_input(input)
part1()
