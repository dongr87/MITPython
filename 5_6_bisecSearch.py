def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return aStr == char

    midIndex = len(aStr)/2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    elif char<midChar:
        return isIn(char,aStr[:midIndex])
    elif char>midChar:
        return isIn(char,aStr[midIndex:])

print isIn('r', 'hnr')
print isIn('a','')
