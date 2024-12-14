from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    lines = codeInput.find_all_ints_in_lines()
    result = list()
    for idx in range(0, len(lines), 4):
        game = dict()
        # Expand the input (Ax, Bx, Tx) and (Ay, By, Ty)
        game["x"] = (lines[idx][0], lines[idx + 1][0], lines[idx + 2][0])
        game["y"] = (lines[idx][1], lines[idx + 1][1], lines[idx + 2][1])
        result.append(game)
    return result


# def find_factors(num :int) -> set:
#     for idx in range(1, n // 2 + 1)


def get_combos(game) -> tuple:
    # Break the game values in to x / y values
    x_values = game["x"]
    y_values = game["y"]
    Ax, Bx, Tx = x_values
    Ay, By, Ty = y_values

    # Caclulate the solutions for A & B given the x & y vaules
    # I had to use ChatGPT to do the math for me. I don't remember how to math this.

    detM = Ax * By - Bx * Ay
    A = (By * Tx - Bx * Ty) // detM
    B = (-Ay * Tx + Ax * Ty) // detM

    # Now let's make sure the results are valid integers and not rounded
    if A * Ax + B * Bx == Tx and A * Ay + B * By == Ty:
        print(f"Valid: {(A,B)}")
        return (A, B)
    else:
        print("Invalid")
        return None


def part1(dataInput):
    games = dataInput
    total_tokens_spent = 0
    for game in games:
        poss_combos = get_combos(game)
        if poss_combos == None:
            continue
        A, B = poss_combos
        if A <= 100 and B < 100:
            total_tokens_spent += A * 3 + B
    print(total_tokens_spent)


def part2(dataInput):
    games = dataInput.copy()
    total_tokens_spent = 0
    for game in games:
        Ax, Bx, Tx = game["x"]
        Ay, By, Ty = game["y"]
        Tx += 10000000000000
        Ty += 10000000000000
        game2 = {"x": (Ax, Bx, Tx), "y": (Ay, By, Ty)}
        poss_combos = get_combos(game2)
        if poss_combos == None:
            continue
        A, B = poss_combos
        total_tokens_spent += A * 3 + B
    print(total_tokens_spent)


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
