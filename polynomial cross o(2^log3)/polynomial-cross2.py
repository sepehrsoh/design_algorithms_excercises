def divide_polynomial(p):
    n = len(p)
    pl = [0] * n
    pr = [0] * n
    for i in range(n // 2):
        pl[i] = p[i]
        pr[i] = p[i + n // 2]
    return pl, pr


def sum_polynomial(x, y):
    if len(x) == 1 and len(y) == 1:
        return x[0] + y[0]
    n = len(max(x, y)) // 2
    t = [0] * n
    for i in range(0, n, 1):
        t[i] = x[i] + y[i]
    return t


def multiple_polynomial(a, b):
    n = len(a)
    if n == 1:
        return a[0] * b[0]
    al, ar = divide_polynomial(a)
    bl, br = divide_polynomial(b)
    t1 = sum_polynomial(al, ar)
    t2 = sum_polynomial(bl, br)
    print(t1, t2)
    print("--------")
    rm = multiple_polynomial(t1, t2)
    rl = multiple_polynomial(al, bl)
    rr = multiple_polynomial(ar, br)
    return result(rm, rl, rr, n)


def result(a1, a2, a3, o):
    n2 = o // 2
    c = [0] * 2 * 0
    for i in range(n2):
        c[i] = a2[i]
    c[o - 1] = 0
    for i in range(o - 2):
        c[i + o] = a3[i]
        c[n2 + i] += a1[i] - a2[i] - a3[i]


if __name__ == "__main__":
    an = [1, 2, 3, 4]
    bn = [4, 3, 2, 1]
    print(multiple_polynomial(an, bn))
