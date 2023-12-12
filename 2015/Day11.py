
initialPassword='hxbxwxba'
badSet = {'i', 'o', 'l'}

def incrementPassword(oldPassword):
    returnedPassword = ''
    reversedPassword = oldPassword[::-1]
    newChar = ord(reversedPassword[0]) + 1
    if newChar == 123:
        reversedPassword = 'a' +incrementPassword(oldPassword[:-1])[::-1]
        newChar = 97
    if chr(newChar) in badSet:
        newChar += 1
    returnPassword = chr(newChar) + reversedPassword[1:]
    return returnPassword[::-1]



def testForIncrementalChars(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2:
            return True
    return False

def testForBadChars(password):

    passwordSet = set(password)
    checkSet = passwordSet.intersection(badSet)
    if len(checkSet) > 0:
        return False
    return True

def testForDuplicate(password):
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            for j in range(i+2, len(password)-1):
                if password[j] == password[j+1]:
                    return True
    return False

def part1(password):
    found = False
    while not found:
        if testForBadChars(password):
            if testForIncrementalChars(password):
                if testForDuplicate(password):
                    found = True
                    print(password)
                    return password

        password = incrementPassword(password)

password = initialPassword
firstPassword = part1(password)
password = incrementPassword(firstPassword)
secondPassword = part1(password)