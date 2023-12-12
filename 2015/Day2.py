inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day2-Input.txt"
# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day2-Input-Alt.txt"

def readInput():
    f = open(inputFile, "r")
    presents = []
    for line in f.readlines():
        present = line.rstrip().split("x")
        present = [int(x) for x in present]
        presents.append(present)  
    return presents      

def Part1(presents):
    totalPaper = 0
    for present in presents:
        l, w, h = present
        present.sort()
        smallest, secondSmallest = present[0], present[1]
        paper = 2*l*w + 2*w*h + 2*h*l + smallest*secondSmallest
        totalPaper += paper
        # print(l, w, h, smallest, paper, totalPaper)
    return totalPaper

def Part2(presents):
    totalRibbon = 0
    for present in presents:
        l, w, h = present
        present.sort()
        smallest, secondSmallest = present[0], present[1]
        ribbon = 2*(smallest + secondSmallest) + l*w*h
        totalRibbon += ribbon
        # print(l, w, h, smallest, ribbon, totalRibbon)
    return totalRibbon


presents = readInput()
print(Part1(presents))
print(Part2(presents))
