import random
import math


def first():
    inputString = input("Enter the dimension the square matrix should have:")
    matrixSize = int(inputString)
    print("Matrix is being generated with size ", matrixSize, "\n")

    # Initialize matrix
    matrix = [random.choices(range(1, 15), k=matrixSize) for _ in range(matrixSize)]

    # matrix = []
    # loop through rows and columns and set pseudorandom numbers
    for i in range(matrixSize):  # loop for row entries
        a = []
    for j in range(matrixSize):  # loop for column entries
        randomInteger = random.randint(0, matrixSize)
        a.append(randomInteger)
        matrix.append(a)

    # function to print matrix
    def printMatrix():
        for i in range(matrixSize):

            for j in range(matrixSize):
                digitlength = int(math.log10(matrix[i][j]))+1  #laenge der Zahl berechnen für diversen Formatoutput
                if digitlength == 2: print(matrix[i][j], end=" ") #wenn Laenge 2 Zahlen betraegt, printe 1 Leerzeichen
                else: print(matrix[i][j], end="  ") #ansonsten zwei Leerzeichen

            print()

    def calculateDifference(matrixArray, sizeofmatrix):

        # Initialisieren von Zaehlern
        upcount = 0
        columncount = 0
        reversecount = sizeofmatrix - 1  # index ist zerobased
        sumOfFirstDiagonal = 0
        sumOfSecondDiagonal = 0

        while (upcount < sizeofmatrix):
            # if rowcount == columncount:
            sumOfFirstDiagonal = sumOfFirstDiagonal + matrixArray[upcount][upcount]
            upcount = upcount + 1

        # upcount zuruecksetzen
        upcount = 0
        while (reversecount >= 0):
            sumOfSecondDiagonal = sumOfSecondDiagonal + matrixArray[upcount][reversecount]
            reversecount = reversecount - 1
            upcount = upcount + 1

        return abs(sumOfFirstDiagonal - sumOfSecondDiagonal)

    printMatrix()

    print("\n The absolute difference of the two diagonals is: ", calculateDifference(matrix, matrixSize))


# task12 main
if __name__ == '__main__':
    first()


