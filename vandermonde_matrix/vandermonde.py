import numpy as np


# making square matrix
def sq_mat(n):
    return np.ones((n, n))


def Vandermonde(w, n):
    W = sq_mat(n)
    for i in range(n):
        for j in range(n):
            W[i][j] = w ** (i * j)
    return W


if __name__ == '__main__':
    print(Vandermonde(2, 4))
# result :
# [[  1.,   1.,   1.,   1.],
#  [  1.,   2.,   4.,   8.],
#  [  1.,   4.,  16.,  64.],
#  [  1.,   8.,  64., 512.]]
