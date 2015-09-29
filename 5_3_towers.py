def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    count = 0
    if n == 1:
        printMove(fr, to)
        count += 1
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
    print count

Towers(3,'f','t','s')

# Towers(10,'f','t','s')
