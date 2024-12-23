from AOC import AOC


def parse_input(codeInput: AOC):
    graph = codeInput.read_graph()
    return graph


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = 16, 2024

    # global data
    codeInput = AOC(codeDate, codeYear, test=True)
    dataInput = parse_input(codeInput)


if __name__ == "__main__":
    main()
