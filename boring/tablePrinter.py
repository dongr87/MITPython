#! python3
# tablePrinter.py - Take 2 dimentional lists, print it out as table

def tablePrinter(tableData):

    # define colWidth to detect the max width of each column
    colWidth =[0] * len(tableData)

    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colWidth[i]:
                colWidth[i] = len(item)

    # print out the table
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidth[col]), end = ' ')
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


if __name__ == '__main__':
    tablePrinter(tableData)


