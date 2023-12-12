# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day5-Input-Test.txt"
inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day5-Input"

vowels = set(['a', 'e', 'i', 'o', 'u'])
badStrings = ['ab', 'cd', 'pq', 'xy']

def getStringsFromFile(filename):
    strings = list()
    f = open(filename, "r")
    for line in f.readlines():
        # print(line)
        strings.append(line.rstrip())
    return strings

def part1():

    def checkIfNice(string):
        
        #Check number of Vowels
        vowelCount = 0   
        for vowel in vowels:
            vowelCount += string.count(vowel)
        if vowelCount < 3:
            return False

        # Check for a repeated letter
        foundDup = False
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                foundDup = True
        if not foundDup:
            return False

        # Check for bad letter
        for i in range(len(string)-1):
            if string[i:i+2] in badStrings:
                return False
        
        return True

def part2():

    def checkIfNice(string):
        
      # Check for a duplicate pair
        dupFound = False
        for i in range(len(string) - 3):
            checkString=string[i:i+2]
            for j in range(i+2, len(string)-1):
                checkString2 = string[j:j+2]
                if checkString == checkString2:
                    dupFound = True
        if not dupFound:
                return False

        repeatLetter = False
        for i in range(len(string) - 2):
            if string[i] == string[i+2]:
                repeatLetter = True
        if not repeatLetter:
            return False
        
        return True

    niceList = []
    wholeList = getStringsFromFile(inputFile)
    for nameString in wholeList:
        if checkIfNice(nameString):
            niceList.append(nameString)
        print(nameString, checkIfNice(nameString))
    return len(niceList)

# print(part1())
print(part2())