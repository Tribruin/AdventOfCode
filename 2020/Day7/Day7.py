from timeit import timeit
import re

INPUT_FILE = "Day7-Input.txt"
BAG_TO_FIND = "shiny gold"


def read_file():
    with open(INPUT_FILE) as f:
        lines = f.readlines()

    all_bag_rules = dict()
    for line in lines:
        bag_name, bag_rules = re.split(" contain ", line.strip(".\n"))
        bag_name = re.sub(" bags*", "", bag_name).strip()
        if bag_rules == "no other bags":
            all_bag_rules[bag_name] = {"none": 0}
        else:
            tmp_dict = {}
            bag_rules_split = re.split(", ", bag_rules)
            for bag_rule in bag_rules_split:
                qty, color = re.split(" ", bag_rule, maxsplit=1)
                color = re.sub(" bags*", "", color)
                tmp_dict[color] = int(qty)
            all_bag_rules[bag_name] = tmp_dict
    return all_bag_rules


def part1():
    def check_bag(color):

        if BAG_TO_FIND in all_bag_rules[color].keys():
            return True
        elif "none" in all_bag_rules[color].keys():
            return False
        else:
            total_result = False
            for bag_contents in all_bag_rules[color]:
                total_result = total_result or check_bag(bag_contents)
            return total_result

    bags_that_work = list()
    for bag_color in all_bag_rules.keys():
        if check_bag(bag_color):
            bags_that_work.append(bag_color)
    print(len(bags_that_work))


def part2():
    def bags_inside(color):
        total_bags = 0
        if "none" in all_bag_rules[color]:
            return 1
        else:
            for key, value in all_bag_rules[color].items():
                total_bags = value * bags_inside(key) + total_bags
            return total_bags + 1  # +1 to include the enclosure bag

    total_bags = bags_inside(BAG_TO_FIND)
    print(total_bags - 1)
    # Remove the initial shiny gold bag as we only
    # want bags inside that bag


all_bag_rules = read_file()
print(timeit(part1, number=1))
print(timeit(part2, number=1))
