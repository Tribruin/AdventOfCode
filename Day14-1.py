#!/usr/bin/env python

from operator import itemgetter

<<<<<<< HEAD
inputFile = "/Users/rblount/Scripts/AdventOfCode/2019/Day14-Input.txt"
spareORE = 0


=======
inputFile = "/Users/rblount/Scripts/AdventOfCode/Day14-Input.txt"
spareORE = 0

>>>>>>> e655167b449fbc2425eecf662d9373e78534458b
def getInput():
    f = open(inputFile, "r")
    lines = f.readlines()

    receipe = {}
    for line in lines:
        reactionInput, reactionOutput = line.split(" => ")
        reactionQty, reactionName = reactionOutput.split(" ")
        listOfInputs = {}
        reactionInputs = reactionInput.split(", ")
        for reactions in reactionInputs:
            qty, name = reactions.rstrip().split(" ")
            listOfInputs[name] = int(qty)
<<<<<<< HEAD
        receipe[reactionName.rstrip()] = {
            "Qty": int(reactionQty),
            "input": listOfInputs,
            "refined": 0,
            "unused": 0,
        }

    return receipe


def getRequiredInput(product, name, qtyRequired):

    totalORE = 0
    inputs = product["input"]
    perRefinemantQty = product["Qty"]
=======
        receipe[reactionName.rstrip()] = {'Qty' : int(reactionQty), 'input': listOfInputs, 'refined': 0, 'unused': 0}

    return receipe

def getRequiredInput(product, name, qtyRequired):

    totalORE = 0
    inputs = product['input']
    perRefinemantQty = product['Qty']
>>>>>>> e655167b449fbc2425eecf662d9373e78534458b
    for key, value in inputs.items():
        print(f"Checking {name} for {key}")
        if key == "ORE":
            print(f" {perRefinemantQty} {name} needs {value} of {key}")
<<<<<<< HEAD
            return value
        else:
            newOre = getRequiredInput(steps[key], key, value)
            print(f" {perRefinemantQty} {name} needs {value} of {key}")
            totalORE += qtyRequired * (perRefinemantQty * newOre)
    return totalORE


steps = getInput()
print(steps)
startingReaction = steps["FUEL"]
totalOreNeeded = getRequiredInput(startingReaction, "FUEL", 1)
=======
            return value 
        else:
            newOre = getRequiredInput(steps[key], key, value)
            print(f" {perRefinemantQty} {name} needs {value} of {key}")
            totalORE += qtyRequired* (perRefinemantQty * newOre)
    return totalORE

steps = getInput()
print(steps)
startingReaction = steps['FUEL']
totalOreNeeded = getRequiredInput(startingReaction, 'FUEL', 1)
>>>>>>> e655167b449fbc2425eecf662d9373e78534458b
print(totalOreNeeded)
