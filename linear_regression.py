from random import randint


def is_vector(v):
    if (not v) or (list != type(v)):
        return False
    for i in v:
        if int != type(i):
            return False
    return True


def multiply_vectors(v1, v2):
    if (not is_vector(v1)) or (not is_vector(v2)):
        raise Exception('Invalid vectors: {} {}'.format(v1, v2))
    if len(v1) != len(v2):
        raise Exception('Vectors in different length')
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def flip_matrix(m):
    if (not m) or (not is_matrix(m)):
        raise Exception('Invalid matrix: {}'.format(m))
    return [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]


def is_matrix(m):
    if (not m) or (list != type(m)):
        return False
    for v in m:
        if not is_vector(v):
            return False
    return True


def multiply_matrices(m1, m2):
    if (not is_matrix(m1)) or (not is_matrix(m2)):
        raise Exception('Invalid matrices: {} {}'.format(m1, m2))
    if len(m1[0]) != len(m2):
        raise Exception('Matrices incompatible sizes')
    return [[multiply_vectors(v1, v2) for v2 in flip_matrix(m2)] for v1 in m1]


def print_matrix(m):
    for r in m:
        print(r)


def generate_vector(length):
    return [randint(0, 9) for _ in range(length)]


def generate_matrix(row, col):
    return [generate_vector(col) for _ in range(row)]


def main():
    common = randint(1, 10)
    m1 = generate_matrix(randint(1, 10), common)
    m2 = generate_matrix(common, randint(1, 10))
    print('m1:')
    print_matrix(m1)
    print('m2:')
    print_matrix(m2)
    m = multiply_matrices(m1, m2)
    print('result:')
    print_matrix(m)


if __name__ == '__main__':
    main()
