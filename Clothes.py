"""
2.Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

# класс Clothes
class Clothes:

    # конструктор класса Clothes
    def __init__(self, type1, demention):
        # Инициализация свойств.
        try:
            if type(type1) == str and (type1.lower() == "coat" or type1.lower() == "suit"):
                self.type1 = type1
                if self.type1 == "coat":
                    self.v = demention
                else:
                    self.h = demention
            else:
                assert print(f"{type1}:Wrong type of Clothes. Supports types: 'coat', 'suit'")
        except: TypeError


    def get_square(self):
        try:
            if self.type1 == "coat":
                return self.v / 6.5 + 0.5
            elif self.type1 == "suit":
                return 2 * self.h + 0.3
        except:
            print("Can't calc square")
            return -1



a = Clothes(2090, 100)
b = Clothes("coat", 43)
c = Clothes("suit", 49)
d = Clothes("dress", 50)
print(a.get_square())
print(b.get_square())
print(c.get_square())
