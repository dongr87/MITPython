#! python3
# pwValidator - a password validator to detect how strong the password is

'''
Rules:
8 char long
both uppercase and lowercase char
at least 1 digit
'''

import re

def pwValidator(pw):

    regexCharLength = re.compile(r'\S{8,}')
    regexUpper = re.compile(r'[A-Z]+?')
    regexLower = re.compile(r'[a-z]+?')
    regexDigit = re.compile(r'[0-9]+?')

    if regexCharLength.search(pw) is None:
        return False
    elif regexUpper.search(pw) is None:
        return False
    elif regexLower.search(pw) is None:
        return False
    elif regexDigit.search(pw) is None:
        return False
    else:
        return True



if __name__ == '__main__':

    test_pws= ['testpw',
    'Testpw',
    'TESTPW',
    'TESTPW123',
    'Testpw123',
    'TESTPW123!@#',
    'Tb1@Tb1@',
    'TestPW123',
    '!@345ssfe@#23T4']



    for pw in test_pws:
        if pwValidator(pw):
            print(pw + ' -- Valid')
        else:
            print(pw + ' -- INVALID')



