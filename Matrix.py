"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
"""

class Matrix():
    def __init__(self, list_of_list):
        #matrix_dem_check = [row_i for row_i in range(len(list_of_list)-1) if len(list_of_list[row_i]) == len(list_of_list[row_i+1])]
        #print(matrix_dem_check)
        #if len(matrix_dem_check) == len(list_of_list):
        self.matr = list_of_list
        self.row_len = max([len(row) for row in list_of_list if type(row) == list])
        self.col_len = len(list_of_list)

    def __str__(self):
        res = ""
        for row in self.matr:
            res += "".join(["|", "".join([str(item) + " " for item in row]), "|\n"])
        return res

    def __add__(self, other):
        try:
            if self.row_len == other.row_len and self.col_len == other.col_len and type(other) == Matrix:
                res = []
                for col_l in range(self.col_len):
                    res_r = []
                    for row_l in range(self.row_len):
                        try:
                            res_r.append(self.matr[col_l][row_l] + other.matr[col_l][row_l])
                        except: IndentationError
                    res.append(res_r)
        except: TypeError(f"Wrong type of {self} or {other}")
        return Matrix(res)



my_matr1 = Matrix([[1, 2, 23], [3, 4, 4], [21, 4, 1]])
my_matr2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(my_matr1)
my_matr3 = my_matr1 + my_matr2
print(type(my_matr1))
print(my_matr3)
