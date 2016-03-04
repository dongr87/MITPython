# https://docs.google.com/forms/d/13RNJl0tzQq0vfGXdOG1zjT6zZO2Vl7HUPDds9Tw4ixo/viewform?c=0&w=1
# source page of this exercise

def nfruits(pDict, pString):
    for s in pString:
        pDict[s] -= 1
        for key in pDict.keys():
            if key is not s:
                pDict[key] += 1
    return max(pDict.values())


def Nfruits(initials, fpattern):
    '''
    (dict, list)  -> int
    initials: Initial quantities of fruits with Python
    fpattern: Pattern in which fruits are eaten as observed by Cobra

    Returns the maximum quantity out of the different
    types of fruits that is available with Python when he has reached MIT.
    '''
    #Shallow copy of initial quantities
    quantities = initials.copy()

    for featen in fpattern[:-1]:

        #Update all fruit quantities
        for fruit in quantities:
            quantities[fruit] += 1

        #Reduce quantity by 1 for eating and 1 for updating
        quantities[featen] -= 2

    #Handling last fruit eaten
    flast = fpattern[-1]
    quantities[flast] -= 1

    return max(quantities.values())

