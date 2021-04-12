"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex():
    def __init__(self, real, image):
        if type(real) == int and type(image) == int:
            self.real = real
            self.image = image
    def __str__(self):
        if self.image >= 0:
            return str(self.real)+"+"+str(self.image)+"j"
        elif self.image < 0:
            return str(self.real) + str(self.image) + "j"

    def __add__(self, other):
        return Complex((self.real + other.real), (self.image + other.image))
    def __mul__(self, other):
        a = self.real * other.real
        b = self.image * other.image * (-1)
        print(self.image, other.image, (-1), b)
        c = self.real * other.image
        d = self.image * other.real
        return Complex((a + b),(c + d))

a = Complex(2, 1)
b = Complex(3, 4)
print(b)
print("+")
print(a)
c = a + b
print("=====")
print(c)
print()
print(b)
print("*")
print(a)
c = a * b
print("=====")
print(c)