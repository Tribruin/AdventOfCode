from AOC import AOC, getDateYear, moveOffets, getMaxYMaxX, addTuples
from time import sleep
from TerminalColors import *


testing = True
y_max = x_max = 0


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    subpos = (0, 0)
    walls = list()
    boxes = list()
    for y, line in enumerate(lines):
        if line == "":
            # Break at the empty line
            final_line = y
        for x, symbol in enumerate(line):
            match symbol:
                case "@":
                    subpos = (y, x)
                case "#":
                    walls.append((y, x))
                case "O":
                    boxes.append((y, x))

    moves = "".join(lines[final_line + 1 :])
    global y_max, x_max
    y_max, x_max = getMaxYMaxX(lines[:final_line])
    return (subpos, walls, boxes, moves)


def part1(dataInput):

    def printMap(subpos, walls, boxes, move):
        print(f"{CLEAR}")
        for y in range(y_max):
            for x in range(x_max):
                if (y, x) == subpos:
                    print(f"{BWHITE}{move}{ENDCOLOR}", end="")
                elif (y, x) in walls:
                    print(f"{BRED}#{ENDCOLOR}", end="")
                elif (y, x) in boxes:
                    print(f"{BBLUE}O{ENDCOLOR}", end="")
                else:
                    print(".", end="")
            print()
        print()
        sleep(0.5)

    def moveBoxes(pos, walls, boxes, move):
        new_boxes = boxes.copy()
        new_pos = addTuples(pos, moveOffets[move])
        if new_pos in walls:
            # print(f"Can't move box {move} to {new_pos}")
            return new_boxes
        elif new_pos in boxes:
            new_boxes = moveBoxes(new_pos, walls, boxes, move)
            if new_boxes == boxes:
                # print(f"Can't move box {move} to {new_pos}")
                return new_boxes

        # print(f"Moving box: {pos} {move} {new_pos}")
        new_boxes.append(new_pos)
        new_boxes.remove(pos)
        return new_boxes

    def makeMove(move, pos, walls, boxes):
        move_offset = moveOffets[move]
        new_pos = addTuples(pos, move_offset)
        if new_pos in walls:
            # print(f"Can't move: {move} to {new_pos}")
            new_pos = pos
        elif new_pos in boxes:
            new_boxes = moveBoxes(new_pos, walls, boxes, move)
            if new_boxes == boxes:
                # print(f"Can't move: {move} to {new_pos}")
                return pos, boxes
            # print(f"Moving {pos} {move} {new_pos}")
            return new_pos, new_boxes
        else:
            # print(f"Moving {pos} {move} {new_pos}")
            pass
        return new_pos, boxes

    subpos, walls, boxes, moves = dataInput
    print("Iniital Map & Position")
    printMap(subpos, walls, boxes, "@")
    for move in moves:
        # print(f"Moving {move}")
        subpos, boxes = makeMove(move, subpos, walls, boxes)
        printMap(subpos, walls, boxes, move)

    gps_total = 0
    for box in boxes:
        y, x = box
        gps_total += 100 * y + x
    print(gps_total)


def part2(dataInput):

    def printMap(subpos, walls, boxes, move):
        boxes_left, boxes_right = boxes
        for y in range(y_max):
            for x in range(x_max):
                if (y, x) == subpos:
                    print(f"{BWHITE}{move}{ENDCOLOR}", end="")
                elif (y, x) in walls:
                    print(f"{BRED}#{ENDCOLOR}", end="")
                elif (y, x) in boxes_left:
                    print(f"{BBLUE}[{ENDCOLOR}", end="")
                elif (y, x) in boxes_right:
                    print(f"{BBLUE}]{ENDCOLOR}", end="")
                else:
                    print(".", end="")
            print()
        print()

    def moveBoxes(pos, walls, double_boxes, move):
        lft_boxes, rgt_boxes = double_boxes
        new_lft_boxes = lft_boxes.copy()
        new_rgt_boxes = rgt_boxes.copy()
        moveValue = moveOffets[move]
        match move:
            case "<":
                box_left = addTuples(pos, moveValue)
                new_pos = addTuples(box_left, moveValue)
                if new_pos in walls:
                    print(f"Can't move box {move} to {new_pos}")
                    return (new_lft_boxes, new_rgt_boxes)
                elif new_pos in right_boxes:
                    pass

                new_lft_boxes.append(new_pos)
                new_lft_boxes.remove(box_left)
                new_rgt_boxes.append(box_left)
                new_rgt_boxes.remove(pos)
                return (new_lft_boxes, new_rgt_boxes)

            case ">":
                box_right = addTuples(pos, moveValue)
                new_pos = addTuples(box_right, moveValue)
                if new_pos in walls:
                    print(f"Can't move box {move} to {new_pos}")
                    return (new_lft_boxes, new_rgt_boxes)
                elif new_pos in lft_boxes:
                    new_lft_boxes, new_rgt_boxes = moveBoxes(
                        new_pos, walls, double_boxes, move
                    )
                if new_lft_boxes == left_boxes and new_rgt_boxes == right_boxes:
                    new_rgt_boxes.append(new_pos)
                    new_rgt_boxes.remove(box_right)
                    new_lft_boxes.append(box_right)
                    new_lft_boxes.remove(pos)
                return (new_lft_boxes, new_rgt_boxes)

        # Start of main function
        new_boxes = double_boxes.copy()
        new_pos = addTuples(pos, moveOffets[move])
        if new_pos in walls:
            print(f"Can't move box {move} to {new_pos}")
            return new_boxes
        elif new_pos in double_boxes:
            new_boxes = moveBoxes(new_pos, walls, new_boxes, move)
            if new_boxes == double_boxes:
                print(f"Can't move box {move} to {new_pos}")
                return new_boxes

        print(f"Moving box: {pos} {move} {new_pos}")
        new_boxes.append(new_pos)
        new_boxes.remove(pos)
        return new_boxes

    def makeMove(move, pos, walls, double_boxes):
        left_boxes, right_boxes = double_boxes
        move_offset = moveOffets[move]
        new_pos = addTuples(pos, move_offset)
        if new_pos in walls:
            print(f"Can't move: {move} to {new_pos}")
            new_pos = pos
        elif new_pos in left_boxes + right_boxes:
            new_boxes = moveBoxes(new_pos, walls, double_boxes, move)
            if new_boxes == double_boxes:
                print(f"Can't move: {move} to {new_pos}")
                return pos, double_boxes
            print(f"Moving {pos} {move} {new_pos}")
            return new_pos, new_boxes
        else:
            print(f"Moving {pos} {move} {new_pos}")
        return new_pos, double_boxes

    # Start main seciton of Part 2
    subpos, walls, boxes, moves = dataInput
    subpos = (subpos[0], subpos[1] * 2)
    global y_max, x_max
    x_max = 2 * x_max
    walls = [pos for (y, x) in walls for pos in [(y, 2 * x), (y, 2 * x + 1)]]
    left_boxes = list()
    right_boxes = list()
    for box in boxes:
        y, x = box
        left_boxes.append((y, 2 * x))
        right_boxes.append((y, 2 * x + 1))
    double_boxes = (left_boxes, right_boxes)

    print("Iniital Map & Position")
    printMap(subpos, walls, double_boxes, "@")
    for move in moves:
        print(f"Moving {move}")
        subpos, double_boxes = makeMove(move, subpos, walls, double_boxes)
        printMap(subpos, walls, double_boxes, move)
    gps_total = 0
    for box in boxes:
        y, x = box
        gps_total += 100 * y + x
    print(gps_total)


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
