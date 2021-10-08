def mul(p, q):
    n = len(p)
    m = len(q)
    x = [0] * (m + n - 1)
    for i in range(n):
        for j in range(m):
            x[i + j] += p[i] * q[j]
    return x


if __name__ == '__main__':
    b = [1, 2, 3]
    c = [6, 5, 0, 2]
    print(mul(b, c))

# result : [6, 17, 28, 17, 4, 6]
