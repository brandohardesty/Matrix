import matrix

def main():

    m = matrix.matrix(2, 2)
    inverseMatrix = matrix.matrix(3,3)
    a = [[201, -101], [-400, 201]]
    b = [[100], [-100]]

    c = [[1, -1, 0], [-2, 2, -1], [0, 1, -2]]
    n = matrix.matrix(2, 1)
    m.setElements(a)
    n.setElements(b)
    inverseMatrix.setElements(c)
    print("Gauss Jordan Elimination: ")
    m.gaussJordan(n)


if __name__ == "__main__":
    main()