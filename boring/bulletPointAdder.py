#! python3
# bulletPointAdder.py - a script to add * for each line in clipboard

'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars

==>

* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
'''


import pyperclip

def bulletPointAdder():
    text = pyperclip.paste()

    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]
    bulletedText = ('\n').join(lines)

    pyperclip.copy(bulletedText)


# lines for testing
"""
text = '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

print('printing text...\n' + text)
print('printing bulletedText...\n' + bulletedText)
"""

if __name__ == '__main__':
    bulletPointAdder()
