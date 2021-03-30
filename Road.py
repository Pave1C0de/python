"""
2. Реализовать класс Road (дорога).

    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра
    дороги асфальтом, толщиной в 1 см * число см толщины полотна;
    проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т. --> не правильные размерности в задании, если как здесь - то результат будет (м**3)*кг, а не т
"""

class Road:
    def __init__(self, length, width):
        self._length = length           #m
        self._width = width             #m
        self.__mass_1_m_sq_hight = 25   #(kg/cm)/(m**2)
        self.__thickness = 5            #cm
    def calc_all_mass(self):
        mass = self._length * self._width * self.__mass_1_m_sq_hight * self.__thickness
        print(f"{self._width}m * {self._length}m * {self.__mass_1_m_sq_hight}(kg/cm)/(m**2) * {self.__thickness}cm = {mass/1000}т")
        return mass


e95 = Road(20, 5000)
print(e95.calc_all_mass())
