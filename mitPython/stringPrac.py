
def sharp(x):
    '''
    (int)  -> int
    x: an integer as the base of 'sharp' operation

    Return the value of x#
    '''
    if x == 2:
        return 2
    return sharp(x-1)**x

def ndigits(x):
    '''
    (int)  -> int
    x: an integer which digits is to be evaluate

    Return the number of digits for x
    '''
    if x/10 == 0:
        return 1
    return ndigits(x/10) + 1

Result = ndigits(sharp(7)) + 2* ndigits(sharp(6)) + ndigits(sharp(5)) +  \
    ndigits(sharp(4))
print Result

'''
def nfruits(pDict, pString):
    count = 0
    for s in pString:
        pDict[s] -= 1
        count += 1
        for key in pDict.keys():
            if key is not s and count < len(pString):
                pDict[key] += 1
    return max(pDict.values())

pDict = {'A': 5, 'B': 7, 'C': 8, 'D': 11, 'E': 4}
pattern = 'AAABBBEECAAABBAACCAADDBBAACDCAAABBBAEACCAEADABCB'
print nfruits(pDict, pattern)
'''

'''
def count(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count = count + 1
    print count

def find(word, letter, start):
    while start < len(word):
        if word[start] == letter:
            return start
        start += 1
    return -1


def count(word, letter, start):
    count = 0
    while start <= len(word):
        if find(word,letter,start) != -1:
            count += 1
            start = find(word,letter,start) + 1
        else:
            break
    print count


fruit = 'apples and bananas'
print find(fruit,'s',4)
count(fruit,'s',6)
'''
