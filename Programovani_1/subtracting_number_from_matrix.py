def print_nice_matrix(matrix, m, n):
    """Printing a matrix in a nice way"""
    for i in range(0, m):
        for j in range(0, n):
            if j == len(matrix[i])-1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=" ")


def find_min_in_matrix(matrix, n):
    """Finding a minimum number in matrix"""
    minimum = float('+inf')
    for i in range(0, m):
        if min(matrix[i]) < minimum:
            minimum = min(matrix[i])
    return minimum


def subtracting_number_from_matrix(matrix, number, m, n):
    """Subtracting a number from a matrix"""
    for i in range(0, m):
        for j in range(0, n):
            matrix[i][j] -= number
    return matrix


# make a dimension of matrix
m, n = map(int, input().split())

# make a matrix of 0
Matrix = [[0 for x in range(n)] for y in range(m)]

# input int values to matrix
for i in range(0, m):
    Matrix[i] = [int(x) for x in input().split()]

# finding a minimum number in matrix
min_of_matrix = find_min_in_matrix(Matrix, n)

# Subtracting a number from a matrix
new_matrix = subtracting_number_from_matrix(Matrix, min_of_matrix, m, n)
print_nice_matrix(new_matrix, m, n)
