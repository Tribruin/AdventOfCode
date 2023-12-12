import TerminalColors

with open("/Users/rblount/Scripts/AdventOfCode/2021/Day15/output.txt") as f:
    output = f.readlines()

with open("/Users/rblount/Scripts/AdventOfCode/2021/Day15/sampleInput.txt") as f:
    sample = f.readlines()

for y in range(len(output)):
    for x in range(len(output[0])):
        if output[y][x] != sample[y][x]:
            print(f"Point: {(x, y)}: Sample {sample[y][x]} Output {output[y][x]}")
