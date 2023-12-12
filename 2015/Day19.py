inputMolecule = "HOHOHO"

inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day19-Input-Replacements-Test.txt"

def readInput(filename):
    f = open(filename, "r")

    replacements = dict()

    for line in f.readlines():
        moleculeReplacement = line.rstrip().split(" => ")
        label = moleculeReplacement[0]
        if label in replacements.keys():
            replacements[label].append(moleculeReplacement[1])
        else:
            replacements[label] = [moleculeReplacement[1]]

    return replacements

def breakInputMolecule(molecule, replacementList):
    singleCharMolecules = list(i for i in molecule if len(i) == 1)
    return singleCharMolecules

def combindMoleculeList(allNewMolecules):
    newMolecules = list()
    for i in range(len(allNewMolecules)):
        newMolecule = ""
        for letter in allNewMolecules[i]:
            newMolecule += letter
        newMolecules.append(newMolecule)
    return list(set(newMolecules))

# Part 1
moleculeList = readInput(inputFile)
# print(moleculeList)
listOfMolecule = breakInputMolecule(inputMolecule, moleculeList)
# print(listOfMolecule)
listOfReplacements = []
for i in range(len(listOfMolecule)):
    # newMolecule = listOfMolecule
    molecule = listOfMolecule[i]
    if molecule in set(moleculeList.keys()):
        for k in moleculeList[molecule]:
            newMolecule = list(listOfMolecule)
            newMolecule[i] = k
            listOfReplacements.append(newMolecule)

# uniqueMolecules = set(listOfReplacements)
uniqueMolecules = combindMoleculeList(listOfReplacements)
# print(listOfReplacements)
print(uniqueMolecules)
