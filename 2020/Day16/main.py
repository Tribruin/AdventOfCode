import sys
from copy import deepcopy
import numpy as np

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")
sys.path.append("/Users/blountr/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

valid_tickets = []


def parse_input(data):
    ticket_rules = {}
    my_ticket = []
    other_tickets = []

    i = 0
    while True:
        if data[i] == "":
            break
        rule_name, rules = data[i].split(": ")
        rules = rules.split(" or ")
        rule1 = [int(x) for x in rules[0].split("-")]
        rule2 = [int(x) for x in rules[1].split("-")]
        ticket_rules[rule_name] = [rule1, rule2]
        i += 1

    data = data[i + 2 :]
    my_ticket = [int(x) for x in data[0].split(",")]

    data = data[3:]
    for line in data:
        ticket = [int(x) for x in line.split(",")]
        other_tickets.append(ticket)

    return ticket_rules, my_ticket, other_tickets


def check_ticket(ticket):
    bad_values = list()
    rule_range = ticket_rules.values()
    for value in ticket:
        valid = False
        for range in rule_range:
            min1, max1, min2, max2 = range[0][0], range[0][1], range[1][0], range[1][1]
            if min1 <= value <= max1 or min2 <= value <= max2:
                valid = True
                break
        if not valid:
            bad_values.append(value)
    return bad_values


def part1():
    bad_values = list()
    global valid_tickets
    # valid_tickets = list()
    for ticket in other_tickets:
        new_bad_values = check_ticket(ticket)
        bad_values += new_bad_values
        if len(new_bad_values) == 0:
            valid_tickets.append(ticket)
    print(sum(bad_values))
    return


def part2():
    global valid_tickets
    ticket_order = {key: [] for key in ticket_rules.keys()}
    tickets_to_check = np.array(valid_tickets)
    for rule in ticket_rules.keys():
        min1, max1, min2, max2 = (
            ticket_rules[rule][0][0],
            ticket_rules[rule][0][1],
            ticket_rules[rule][1][0],
            ticket_rules[rule][1][1],
        )
        for column in range(len(my_ticket)):
            valid = True
            for row in range(len(tickets_to_check)):
                value = tickets_to_check[row][column]
                if not (min1 <= value <= max1 or min2 <= value <= max2):
                    valid = False
                    break
            if valid:
                ticket_order[rule].append(column)

    # for rule in ticket_rules.keys():
    # print(ticket_order)
    final_values = dict()
    columns_found = set()
    all_finished = False
    while not all_finished:
        # for key, value in ticket_order.items():
        #     print(f"Rule: {key} - Valid Columns {len(value)} - {value}")
        all_finished = True
        for key, value in ticket_order.items():
            if len(value) == 1:
                final_values[key] = value[0]
                columns_found.add(value[0])
            else:
                ticket_order[key] = list(set(value).difference(columns_found))
                all_finished = False
    final_number = 1
    for key, column in ticket_order.items():
        if key.startswith("departure"):
            print(f"Key: {key} Column: {column[0]} My Ticket: {my_ticket[column[0]]}")
            final_number *= my_ticket[column[0]]
    print(final_number)


a = AOC(16, test=False)
data = a.read_lines()
ticket_rules, my_ticket, other_tickets = parse_input(data)
part1()
part2()