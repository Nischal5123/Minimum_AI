# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Function to get cofactor of
# matrix[p][q] in temp[][]. n is
# current dimension of matrix[][]
def findCoFactor(matrix, temp, p, q, n):
    i = 0
    j = 0
    # Looping for each element
    # of the matrix
    for row in range(n):

        for col in range(n):

            # Copying into temporary matrix
            # only those element which are
            # not in given row and column
            if (row != p and col != q):

                temp[i][j] = matrix[row][col]
                j += 1
                # Row is filled, so increase
                # row index and reset col index
                if (j == n - 1):
                    j = 0
                    i += 1


# Recursive function for
# finding determinant of matrix.
# n is current dimension of mat[][].
def getDetOfMatrix(matrix, n):
    D = 0  # Initialize result
    # Base case : if matrix
    # contains single element
    if (n == 1):
        return matrix[0][0]

    # To store cofactors
    temp = [[0 for x in range(N)]
            for y in range(N)]
    sign = 1  # To store sign multiplier
    # Iterate for each
    # element of first row
    for f in range(n):
        # Getting Cofactor of matrix[0][f]
        findCoFactor(matrix, temp, 0, f, n)
        D += (sign * matrix[0][f] *
              getDetOfMatrix(temp, n - 1))
        # inverted elements are needs to be added with negative sign.
        sign = -sign
    return D


def isMatrixInvertible(matrix, n):
    if (getDetOfMatrix(matrix, N) != 0):
        return True
    else:
        return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Main Function Code
    matrix = [[1, 2],
              [3, 4]]

    N = 2
    if (isMatrixInvertible(matrix, N)):
        print("Yes")
    else:
        print("No")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
