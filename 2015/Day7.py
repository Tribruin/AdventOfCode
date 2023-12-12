# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day7-Input-Test.txt"
inputFile = "/Users/rblount/Scripts/AdventOfCode/2015/Day7-Input.txt"
wireToFind = "a"


def parseFile(file):
    connections = dict()
    f = open(file, "r")

    for line in f.readlines():
        input = line.rstrip()
        inputs, outputWire = input.split(" -> ")
        connections[outputWire] = dict()
        if inputs.isnumeric():
            connections[outputWire]["value"] = int(inputs)
            connections[outputWire]["operator"] = "None"
        else:
            connections[outputWire]["value"] = None
            if inputs[:3] == "NOT":
                connections[outputWire]["operand1"] = inputs.split(" ")[1]
                connections[outputWire]["operator"] = "NOT"
            else:
                inputSplit = inputs.split(" ")
                # connections[outputWire]['value'] = None
                if len(inputSplit) == 1:
                    connections[outputWire]["operand1"] = inputSplit[0]
                    connections[outputWire]["operator"] = "COPY"
                else:
                    connections[outputWire]["operand1"] = inputSplit[0]
                    connections[outputWire]["operand2"] = inputSplit[2]
                    connections[outputWire]["operator"] = inputSplit[1]

    return connections


def processOperation(operation):
    # Calculate the values of the operands
    # If operand does not exist, skip it
    # If operand is numeric, set the variable
    # if the operand is another wire, check for wire value
    # if the value does not exist, calculate the value first.

    result = operation.get("operand1", None)
    if (not result == None) and (not result.isnumeric()):
        if operations[result]["value"] == None:
            operations[result]["value"] = processOperation(operations[result])
        op1 = operations[result]["value"]
    elif (not result == None) and result.isnumeric():
        op1 = int(result)

    result = operation.get("operand2", None)
    if (not result == None) and (not result.isnumeric()):
        if operations[result]["value"] == None:
            operations[result]["value"] = processOperation(operations[result])
        op2 = operations[result]["value"]
    elif (not result == None) and result.isnumeric():
        op2 = int(result)

    if operation["operator"] == "None":
        returnValue = operation["value"]

    elif operation["operator"] == "AND":
        returnValue = op1 & op2

    elif operation["operator"] == "OR":
        returnValue = op1 | op2

    elif operation["operator"] == "LSHIFT":
        returnValue = op1 << op2

    elif operation["operator"] == "RSHIFT":
        returnValue = op1 >> op2

    elif operation["operator"] == "NOT":
        returnValue = ~op1

    elif operation["operator"] == "COPY":
        returnValue = op1

    if returnValue < 0:
        returnValue += 65536  # Convert Negative to Positive

    return returnValue


# Create the operations array
operations = parseFile(inputFile)

# Find the value of wire 'a' and print it
finalA = operations["a"]["value"] = processOperation(operations["a"])

print(f"a: {finalA}")

# Reset the wires
operations = parseFile(inputFile)

# Set 'b' to a
operations["b"]["value"] = finalA

finalA2 = operations["a"]["value"] = processOperation(operations["a"])

print(f"a: {finalA2}")
