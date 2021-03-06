#! python3

# Check if a serie of number is valid phone number

def isPhoneNumber(text):
    if len(text) != 12: return False
    for i in range(3):
        if not text[i].isdecimal(): return False
    if text[3] != '-': return False
    for i in range(4,7):
        if not text[i].isdecimal(): return False
    if text[7] != '-': return False
    for i in range(8,12):
        if not text[i].isdecimal(): return False

    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

# Find number from a text, by referencing isPhoneNumber function
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone Number Found: ' + chunk)
print('Done')

# using regular expression
import re

# re.compile()
# regexObj.search()
# re.group() to store the found string patterns
# reObj.findall()




phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
# | pipe for multiple matches
# ? question mark for optional matching
# * matching zero or more
# + matching one or more
# {} matching specific Repetitions with curly braces
# greedy and non-greedy matching - {3,5}?
# Character Classes \w\W\d\D\s\S
# make your own Character Classes with []
# Carat Character to make cust classes negative (anti-) ^
# ^ $ carat sign and dollar sign - beginning/end of the searched text
# . dot sign is wildcard (excluding newline)
# re.compile('.*', re.DOTALL) - including newline

# re.compile(r'abc', re.I) or re.compile(r'abc', re.IGNORECASE) - will be case insensitive
# Substituting strings with the sub() method
# re.compile(r'''('multiple line with comments')''', re.VERBOSE)


