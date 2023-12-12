#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import re
from random import shuffle
from typing import Tuple
from AOC import AOC

testing = False


def parse_input(data: AOC) -> Tuple[list, str]:

    replacements = dict()
    lines = data.read_lines()
    i = 0
    while lines[i] != "":
        org_mol, rep_mol = lines[i].split(" => ")
        if org_mol not in replacements.keys():
            replacements[org_mol] = [rep_mol]
        else:
            replacements[org_mol].append(rep_mol)
        i += 1

    orig_molecule = lines[i + 1]

    return (replacements, orig_molecule)


def replace_mols(list_mols, orig_mol) -> list:

    # What the heck am i doing here?
    # mol_pattern = re.compile(r"[A-Z][a-z]*")
    # orig_mol_list = mol_pattern.findall(orig_mol)

    # Split the original molecule in to a list.
    # Hint: Each possible replacement starts with a capital letter
    # followed by zero or more lower case letters
    # Using the Python Regex (re) module to split the string wiht a Regex
    # So O, Rn, etc are possible replacements
    orig_mol_list = re.findall(r"[A-Z][a-z]*", orig_mol)

    replacements_mols = list()

    # loop through the molecule by component (which is a list)
    for x, mol in enumerate(orig_mol_list):
        if mol in list_mols.keys():
            for y in list_mols[mol]:
                new_mol = orig_mol_list.copy()
                new_mol[x] = y
                new_mol_text = "".join(new_mol)
                replacements_mols.append(new_mol_text)
    return list(set(replacements_mols))


def part1(input: tuple):
    list_mols_replacements, starting_mol = input
    print(len(replace_mols(list_mols_replacements, starting_mol)))


def part2(input: Tuple):

    start_mol = "e"

    list_mols, final_mol = input
    list_mol_individual = list()
    for mol, repl_mol in list_mols.items():
        for x in repl_mol:
            list_mol_individual.append((x, mol))

    shuffle(list_mol_individual)
    orig_list_mol = list_mol_individual
    # list_mol_individual.sort(key=lambda x: len(x[0]), reverse=True)

    count = 0
    current_mol = final_mol
    old_current_mol = ""
    while (current_mol != start_mol) and (current_mol != old_current_mol):
        old_current_mol = current_mol
        for repl, orig in list_mol_individual:
            while repl in current_mol:
                current_mol = current_mol.replace(repl, orig, 1)
                count += 1
        list_mol_individual.pop(list_mol_individual.index((repl, orig)))

        print(count)
    if current_mol == start_mol:
        print(count)
    else:
        print("No Solution Found")
        print(current_mol)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = parse_input(data)

    # part1(input)
    part2(input)


if __name__ == "__main__":
    main()
