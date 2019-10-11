import numpy as np


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    b = np.zeros((m+1, n+1))
    b = b.astype('str')
    c = np.zeros((m+1, n+1))

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'left-up'

            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'up'

            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'left'

    return c, b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return

    if b[i][j] == 'left-up':
        print_lcs(b, X, i-1, j-1)
        print(X[i-1])

    elif b[i][j] == 'up':
        print_lcs(b, X, i-1, j)

    else:
        print_lcs(b, X, i, j-1)


def print_lcs_without_b(c, X, Y):
    i = len(X)
    j = len(Y)
    result = []

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
            continue

        if c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    print(result)


X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

c, b = lcs_length(X, Y)

# print_lcs(b, X, len(X), len(Y))

print_lcs_without_b(c, X, Y)