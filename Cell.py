"""
3.
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и округление до целого числа деления клеток, соответственно.

- Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
- Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
- Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
- Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""
# Ячейки в клетке, ну ок)
# На протяжении всего курса крайне низкое качество описания заданий (задания - понимай, как хочешь)!

class Cell:
    def __init__(self, cell_in_cell):
        self.cell_in_cell = cell_in_cell

    @property
    def cell_in_cell(self):
        return self.__cell_in_cell

    @cell_in_cell.setter
    def cell_in_cell(self, cell_in_cell):
        if type(cell_in_cell) == int and cell_in_cell > 0:
            self.__cell_in_cell = cell_in_cell
        else:
            self.__cell_in_cell = 0
            raise print("Wrong cell_in_cell parameter set type or range")

    def __add__(self, other):
        if type(other) == Cell:
            var1 = self.cell_in_cell
            var2 = other.cell_in_cell
            return Cell((var1 + var2))

    def __sub__(self, other):
        try:
            if (type(other) == Cell) and (self.cell_in_cell > other.cell_in_cell):
                return Cell((self.cell_in_cell - other.cell_in_cell))
        except:
            print(f"reduced less then subtracted")


    def __mul__(self, other):
        if (type(other) == Cell) and (other.cell_in_cell > 0 and self.cell_in_cell > 0):
            return Cell(self.cell_in_cell * other.cell_in_cell)
        else:
            raise AttributeError

    def __floordiv__(self, other):
        if (type(other) == Cell) and (other.cell_in_cell > 0 and self.cell_in_cell > 0)  and (self.cell_in_cell > other.cell_in_cell):
            return Cell(self.cell_in_cell // other.cell_in_cell)
        else:
            raise AttributeError

    def __truediv__(self, other):
        if (type(other) == Cell) and (other.cell_in_cell > 0 and self.cell_in_cell > 0) and (self.cell_in_cell > other.cell_in_cell):
            return Cell(int(self.cell_in_cell / other.cell_in_cell))
        else:
            raise AttributeError

    def make_order(self, cell_in_row):
        if type(cell_in_row) == int and cell_in_row > 0:
            full_rows = self.cell_in_cell // cell_in_row
            last_row = self.cell_in_cell % cell_in_row
            show_matrix = ("*" * cell_in_row + "\n") * full_rows + ("*" * last_row + "\n")
            return show_matrix
        else:
            raise AttributeError



c1 = Cell(13)
c2 = Cell(4)
print("MUL")
c3 = c1 * c2
print(c1.cell_in_cell)
print(c2.cell_in_cell)
print(c3.cell_in_cell)
print(c3.make_order(5))

c1 = Cell(13)
c2 = Cell(4)
print("SUM")
c3 = c1 * c2
print(c1.cell_in_cell)
print(c2.cell_in_cell)
print(c3.cell_in_cell)
print(c3.make_order(5))

c1 = Cell(13)
c2 = Cell(4)
print("SUB")
c3 = c1 - c2
print(c1.cell_in_cell)
print(c2.cell_in_cell)
print(c3.cell_in_cell)
print(c3.make_order(5))

c1 = Cell(12)
c2 = Cell(4)
print("DIV")
c3 = c1 // c2
print(c1.cell_in_cell)
print(c2.cell_in_cell)
print(c3.cell_in_cell)
print(c3.make_order(5))

c1 = Cell(12)
c2 = Cell(4)
print("DIV")
c3 = c1 / c2
print(c1.cell_in_cell)
print(c2.cell_in_cell)
print(c3.cell_in_cell)
print(c3.make_order(5))





