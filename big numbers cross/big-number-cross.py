global threshold


def multiple(v, u):
    if v == 0 or u == 0:
        return 0
    n = max(len(str(v)), len(str(u)))
    if n < threshold:
        return v * u
    m = n // 2
    s = pow(10, m)
    x = v // s
    y = v % s
    w = u // s
    z = u % s
    r = multiple(x + y, w + z)
    p = multiple(x, w)
    q = multiple(y, z)
    return p * pow(10, 2 * m) + (r - p - q) * s + q


if __name__ == "__main__":
    threshold = 3
    a = 12345678
    b = 87654321
    print("result: ", multiple(int(a), int(b)))

# example:
# result : 1082152022374638
