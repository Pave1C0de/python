import time

"""
1. Создать класс TrafficLight (светофор).

    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, 
    третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее 
сообщение и завершать скрипт.
"""

class TrafficLight:
    def __init__(self, color="green"):
        try:
            self.__color = color.lower()
        except: TypeError
    def run_light(self):
        wait_time = 0
        if self.__color == "green":
            wait_time = 10
        elif self.__color == "red":
            wait_time = 7
        elif self.__color == "yellow":
            wait_time = 2

        print(f"{self.__color.upper()} light is on:")
        print(f"time: {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec} data: {time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}")
        time.sleep(wait_time)
        print(f"{self.__color} light is off:")
        print(f"time: {time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec} data: {time.localtime().tm_mday}.{time.localtime().tm_mon}.{time.localtime().tm_year}")
        print()

    def running(self):
        while(True):
            if self.__color == "green":
                self.run_light()
                self.__color = "yellow"
                self.run_light()
                self.__color = "red"

            elif self.__color == "red":
                self.run_light()
                self.__color = "yellow"
                self.run_light()
                self.__color = "green"

            elif self.__color == "yellow":
                self.run_light()
                self.__color = "red"


lk = TrafficLight("red")
lk.running()
