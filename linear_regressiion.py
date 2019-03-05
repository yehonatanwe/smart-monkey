def multiply_vectors(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        raise Exception('Vectors in different length')
    result = 0
    for i in range(len(vec_1)):
        result += vec_1[i] * vec_2[i]
    return result


def multiply_matrices(mat_a, mat_b):
    if len(mat_a[0]) != len(mat_b):
        raise Exception('wrong number of rows and columns')
    mat_final = [[], [], []]
    for col_b in range(len(mat_b[0])):
        v = []
        for row_b in range(len(mat_b)):
            v.append(mat_b[row_b][col_b])
        for row_a in range(len(mat_a)):
            mat_final[row_a].append(multiply_vectors(mat_a[row_a], v))
    return mat_final


def main():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    b = [
        [9, 8],
        [7, 6],
        [5, 4]
    ]
    mat_final = multiply_matrices(a, b)
    for row in mat_final:
        print(row)


if __name__ == '__main__':
    main()
