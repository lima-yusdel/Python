#! /usr/bin/env python3
#by Yusdel Lima Lorenzo Prin Prog 2019
#You can multiply two matrices if, and only if, the number of columns in the first matrix equals the number of rows in the second matrix
class Matrix:
    def __build__(self, row, column):
        self.row = row
        self.column = column

        Matrix = [[0 for x in range(column)] for y in range(row)]
        return Matrix


def main():
    try:
        rowInput, columnInput  = str(input()).split(' ')
        numElements = int(rowInput) * int(columnInput)
    except EOFError:
        print('Reached end of file')
        quit()
    MatrixA = Matrix()
    MatrixA = MatrixA.__build__(int(rowInput),int(columnInput))

    List = []
    numbers = []
    for x in range(int(rowInput)):
        try:
            numbers = str(input()).split(' ')
            List.append(numbers)
        except EOFError:
            print('Reached end of file')
            quit()
    data = [val for sublist in List for val in sublist]
    elementList = [ float(x) for x in data]

    count = 0
    for x in range(int(rowInput)):
        for y in range(int(columnInput)):
            MatrixA[x][y] = elementList[count]
            count += 1

    try:
        rowInputB, columnInputB  = str(input()).split(' ')
        numElementsB = int(rowInputB) * int(columnInputB)
    except EOFError:
        quit()

    MatrixB = Matrix()
    MatrixB = MatrixB.__build__(int(rowInputB),int(columnInputB))

    ListB = []
    numbersB = []
    for x in range(int(rowInputB)):
        try:
            numbersB = str(input()).split(' ')
            ListB.append(numbersB)
        except EOFError:
            quit()
    dataB = [valB for sublistB in ListB for valB in sublistB]
    elementListB = [ float(x) for x in dataB]

    countB = 0
    for x in range(int(rowInputB)):
        for y in range(int(columnInputB)):
            MatrixB[x][y] = elementListB[countB]
            countB += 1

    if columnInput == rowInputB:
        MatrixC = [[0 for row in range(int(columnInputB))] for col in range(int(rowInput))]

        for i in range(int(rowInput)):
            for j in range(int(columnInputB)):
                for k in range(int(columnInput)):
                    MatrixC[i][j] += MatrixA[i][k] * MatrixB[k][j]

        for i in range(int(rowInput)):
            for j in range(int(columnInputB)):
                MatrixC[i][j] = round(MatrixC[i][j], 3)
                MatrixC[i][j] = '{0:f}'.format(MatrixC[i][j]).rstrip('0').rstrip('.')




        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in MatrixC]))

    else:
        print('invalid input')

main()
