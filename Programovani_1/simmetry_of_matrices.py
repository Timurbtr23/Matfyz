def symmetry_main_diagonal(_matrix, dimension):
    symmetry = 0
    for i in range(0, dimension):
        for j in range(0, dimension):
            if (_matrix[i][j] == _matrix[j][i]) and (j != i):
                symmetry += 1
    if symmetry == dimension*(dimension-1):
        return 1
    else:
        return 0


def symmetry_secondary_diagonal(_matrix, dimension):
    symmetry = 0
    for i in range(0, dimension):
        for j in range(0, dimension):
            if (i + j != dimension - 1) and (_matrix[i][j] == _matrix[dimension - j - 1][dimension - i - 1]):
                symmetry += 1
    if symmetry == dimension * (dimension - 1):
        return 1
    else:
        return 0


def vertical_symmetry(_matrix, dimension):
    x = dimension % 2
    for i in range(0, dimension):
        for j in range(0, dimension // 2 + x):
            if _matrix[i][j] != _matrix[i][-j - 1]:
                return 0
    return 1


if __name__ == "__main__":
    # input first array of matrix to know dimension
    array = [int(x) for x in input().split()]
    len_of_matrix = len(array)

    # make a matrix of 0
    matrix = [[0 for x in range(len_of_matrix)] for y in range(len_of_matrix)]
    matrix[0] = array

    # input int values to matrix
    for j in range(1, len_of_matrix):
        matrix[j] = [int(x) for x in input().split()]

    answer = [
        symmetry_main_diagonal(matrix, len_of_matrix),
        symmetry_secondary_diagonal(matrix, len_of_matrix),
        vertical_symmetry(matrix, len_of_matrix)
    ]

    print(f'{answer[0]} {answer[1]} {answer[2]}')
