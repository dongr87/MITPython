#! python3
import os

# create file name
print(os.path.join('usr','bin', 'spam'))

# current working directory
os.getcwd()
# change directory
# os.chdir('C:\\Windows\\System32')

# create new folders
# os.makedirs('C:\\delicious\\walnut\\waffles')

print(os.path.abspath('.\\Scripts'))

# Dir name and Base name

# Dirname and Basename split
calPath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calPath)

# parse to os.path.sep to split
calPath.split(os.path.sep)

os.path.isdir('C:\\Windows\\System32')
os.path.isfile('C:\\Windows\\System32')
os.path.exists('C:\\Windows\\System32')




