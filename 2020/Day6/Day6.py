from timeit import timeit
import os
import sys


SCRIPT_PATH = os.path.dirname(sys.argv[0])
# INPUT_FILE_NAME = "Day6-Input-Test.txt"
INPUT_FILE_NAME = "Day6-Input.txt"

INPUT_FILE = f"{SCRIPT_PATH}/{INPUT_FILE_NAME}"


def read_file():
    """Read the input file and generate the list of passports

    Returns:
        List: A list of passport dictionaries
    """
    with open(INPUT_FILE) as f:
        lines = f.readlines()

    group_split = []
    dec_form = []
    for line in lines:
        if line == "\n":
            group_split.append(dec_form)
            dec_form = []
        else:
            dec_form.append(line.strip())

    return group_split


def part1():
    """Compute the sum of all questions answered yes by a group
    dec_froms = list of groups of forms
    cycle through each group of forms and:
        join all group forms together as text string
        create a set of unique questions answered
        sum the length of the individual sets
    """
    print(sum([len(set("".join(i))) for i in dec_forms]))


def part2():
    def check_for_all_questions(group):
        if len(group) == 1:
            return len(group[0])

        else:
            common_questions = set(group[0])
            for form in group[1:]:
                common_questions = common_questions.intersection(set(form))
                if len(common_questions) == 0:
                    return 0
        return len(common_questions)

    running_total = 0
    for group in dec_forms:
        running_total += check_for_all_questions(group)
    print(running_total)


dec_forms = read_file()
print(timeit(part1, number=1) * 1000)
print(timeit(part2, number=1) * 1000)