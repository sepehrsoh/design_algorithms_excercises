import numpy as np


def sq_mat(n):
    return np.ones((n, n))


def Vandermonde(w, n):
    W = sq_mat(n)
    for i in range(n):
        for j in range(n):
            W[i][j] = w ** (i * j)
    return W


# creat complex array from a list
def comp(a):
    for i in range(len(a)):
        a[i] = complex(a[i])
    return np.array(a)


# compute DFT for an array to calculate Fourier Series
def DFT(a):
    typ = False
    for i in a:
        if type(i) == complex:
            typ = True
    if typ:
        a = comp(a)
    n = len(a)
    angel = 2j * np.pi / n
    w = np.exp(-angel)
    W = Vandermonde(w, n)
    return np.matmul(W, a)


if __name__ == '__main__':
    an = [0.5, 0.6366, 0, -0.2122, 0.1273, 0, -0.0909]
    bn = [1 + 2j, 3 + 5j, 2 - 4j, 7, 5, 4j, 1 - 1j]
    # DFT for real numbers
    print("DFT(An): \n", DFT(an), " \n")
    # DFT for complex numbers
    print("DFT(Bn): \n", DFT(bn))
# Result :
# DFT(An):
#  [0.9608     0.91673064 0.32563604 0.02723332 0.02723332 0.32563604
#  0.91673064]
# DFT(Bn):
#  [19.        +6.j         -7.76270908+4.49395921j  5.78985615+1.10991626j
#  -4.02714708-1.60387547j -4.02714708-1.60387547j  5.78985615+1.10991626j
#  -7.76270908+4.49395921j]
