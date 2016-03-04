# To practice if condition and the logic in python.

x = int(raw_input('Enter value of x: '))
y = int(raw_input('Enter value of y: '))
z = int(raw_input('Enter value of z: '))
odd_list = []

#put x,y,z in odd_list if they are odd numbers
def odd_check(num):
    if num%2 == 1:
        odd_list.append(num)

for num in (x, y, z):
    odd_check(num)

if len(odd_list) == 0:
    print 'There are no odd numbers.'
else:
    odd_list.sort()
    print odd_list[-1]
