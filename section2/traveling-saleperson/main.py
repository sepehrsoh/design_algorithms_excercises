import SalePerson as sp

if __name__ == '__main__':
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    sale_person = sp.SalePerson(graph)
    print(sale_person.solve())
