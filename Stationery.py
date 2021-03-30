"""
5. Реализовать класс Stationery (канцелярская принадлежность).
    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print("Stationery сообщение: «Запуск отрисовки»")

class Pen(Stationery):
    def draw(self):
        print("Pen сообщение: «Запуск отрисовки»")


class Pencil(Stationery):
    def draw(self):
        print("Pencil сообщение: «Запуск отрисовки»")


class Handle(Stationery):
    def draw(self):
        print("Handle сообщение: «Запуск отрисовки»")

my_stationary = Stationery("my_title")
my_stationary.draw()

my_pen = Pen("my_title")
my_pen.draw()

my_pencil = Pencil("my_title")
my_pencil.draw()

my_handle = Handle("my_title")
my_handle.draw()