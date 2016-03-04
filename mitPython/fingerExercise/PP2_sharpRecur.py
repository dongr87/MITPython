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
