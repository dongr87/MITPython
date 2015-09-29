def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e

FancyDivide([0,2,4], 0)
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
