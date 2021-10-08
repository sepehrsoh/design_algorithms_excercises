def horner(a, beta):
    b = [0] * len(a)
    b[len(a) - 2] = a[len(a) - 1]
    for i in range(len(a) - 2, -1, -1):
        b[i] = a[i + 1] + beta * b[i + 1]
    return a[0] + beta * b[0]


if __name__ == '__main__':
    a = [7, -2, 0, 5, 4]
    print(horner(a, 2))

# P(x) = 4 x^4 + 5 x^3 - 2 * x + 7
# Q(x) = x - 2
# => beta = 2
# hornier(a,2)
# result : 107
