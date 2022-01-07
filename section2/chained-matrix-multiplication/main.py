import ChaniedMatrix as cm

if __name__ == '__main__':
    chained_matrix = cm.ChainedMatrix([30, 35, 15, 5, 10, 20, 25])
    m = chained_matrix.solve()
    print("Minimum number of multiplications is = {}".format(m))
