#ask the user to input 10 integers, print the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.

itersLeft = 10
odd_list = []

#check if the number is an odd number
def odd_check(num):
    if num%2 == 1:
        return True
    else:
        return False

while (itersLeft > 0):
    itersLeft -= 1
    input_num = int(raw_input('Enter the value: '))
    if (odd_check(input_num)):
        odd_list.append(input_num)

if len(odd_list) == 0:
    print 'There are no odd numbers.'
else:
    odd_list.sort()
    print odd_list[-1]

