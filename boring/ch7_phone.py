#! python3
# Finds phone numbers and email addresses on the clipboard

import pyperclip
import re

text = str(pyperclip.paste())

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension number
    )''', re.VERBOSE)

# email regex - referring https://emailregex.com/
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ sign
    [a-zA-Z0-9.-]+                  # domain name
    (\.[A-z]{2,4})
    )''', re.VERBOSE)

# result will be stored in list matches
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)


for groups in emailRegex.findall(text):
    matches.append(groups[0])


# print out the result and copy it to the clipboard

if (len(matches) > 0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('There is no phone number or email found')
