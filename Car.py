"""
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
class Car:
    def __init__(self, name, color, speed, is_police):
        if type(name) == str and type(color) == str and type(speed) == int and type(is_police) == bool :
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police
        else:
            raise TypeError("Wrong attributes type in __init__()!")

    def go(self, speed):
        if speed > 0:
            self.speed = speed
            print(f"Be carefull car is go")


    def stop(self):
        self.speed = 0
        print(f"Be carefull car is stop")


    def turn(self, direction):
        if direction == "left" or direction == "right":
            print(f"car turn {direction}")
        else:
            print(f"{direction} is wrong side for turn")


    def show_speed(self):
        print(f"Current speed is {self.speed}")


class TownCar(Car):
    def __init__(self, name, color, speed, is_police, speed_limit=60):
        super().__init__(self, name, color, speed, is_police)
        if type(speed_limit) == int and speed_limit > 0:
            self.speed_limit = speed_limit
        else:
            raise TypeError("Wrong attributes type in __init__()!")

    def show_speed(self):
        if self.speed > 60:
            print(f"Current speed more then speed limit {self.speed_limit} km/h : {self.speed}")
        else:
            print(f"Current speed is {self.speed}")


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police, speed_limit=40):
        super().__init__(name, color, speed, is_police)
        if type(speed_limit) == int and speed_limit > 0:
            self.speed_limit = speed_limit
        else:
            raise TypeError("Wrong attributes type in __init__()!")


    def show_speed(self):
        if self.speed > 60:
            print(f"Current speed more then speed limit {self.speed_limit} km/h : {self.speed}")
        else:
            print(f"Current speed is {self.speed}")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)




formula_1 = SportCar("ferrary", "red", 0, False)
formula_1.show_speed()
print(formula_1.color)
formula_1.go(200)
formula_1.go(50)
formula_1.turn("right")
formula_1.go(250)
formula_1.show_speed()
formula_1.stop()
formula_1.show_speed()

milk_car = WorkCar("Zil", "blue", 0, False)
milk_car.go(20)
milk_car.show_speed()
milk_car.go(90)
milk_car.show_speed()
milk_car.stop()
