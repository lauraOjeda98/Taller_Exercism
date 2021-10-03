class Matrix:
    def __init__(self, matrix_string):
        self._matrix_string = matrix_string.split("\n")

    def row(self, index):
        matrix = self._matrix_string

        m = matrix[index-1].split(" ")
        m = list(map(int, m))

        return m

    def column(self, index):
        matrix = self._matrix_string
        m = []

        for i in matrix:
            m.append(i.split(" ")[index-1])
        m = list(map(int, m))

        return m
