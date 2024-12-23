from AOC import AOC, getDateYear
from TerminalColors import *
from itertools import combinations
import networkx as nx

testing = False


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    connections = dict()
    for line in lines:
        line = line.split("-")
        connections[line[0]] = connections.get(line[0], []) + [line[1]]
        connections[line[1]] = connections.get(line[1], []) + [line[0]]
    return connections


def part1(dataInput):
    connections = dataInput
    computers = list(connections.keys())
    computer_trios = list(combinations(computers, 3))
    print(len(computer_trios))

    # Find Valid Trios of three interconnected computers
    valid_trios = list()
    for computer_trio in computer_trios:
        computer1, computer2, computer3 = computer_trio
        if (
            computer2 in connections[computer1]
            and computer3 in connections[computer1]
            and computer3 in connections[computer2]
        ):
            valid_trios.append(computer_trio)
    print(len(valid_trios))

    # Find all computers trios wiht at least one computer that starts with 'T'
    T_computer_trios = list()
    for computer_trio in valid_trios:
        lan_computers = [x[0] for x in computer_trio]
        if "t" in lan_computers:
            T_computer_trios.append(computer_trio)
    print(len(T_computer_trios))
    return valid_trios


def part2(dataInput):
    G = nx.Graph()
    edges = []
    for key, value in dataInput.items():
        for v in value:
            if (v, key) not in edges:
                edges.append((key, v))
    G.add_edges_from(edges)
    largest_clique = nx.algorithms.clique.find_cliques(G)
    max_clique = max(largest_clique, key=len)
    max_clique_str = ",".join(sorted(max_clique))
    print("Maximum Clique:", max_clique_str)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
