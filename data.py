"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Data:
    day = None
    month = None
    year = None
    data = None

    def __new__(cls, args):
        if type(args) == str:
            cls.data = args

    @classmethod
    def parse_data(cls):
        try:
            if type(cls.data) == str and len(cls.data.split("-")) == 3:
                cls.day = int(cls.data.split("-")[0])
                cls.month = int(cls.data.split("-")[1])
                cls.year = int(cls.data.split("-")[2])
        except: TypeError

    @staticmethod
    def check_data(day, month):
        if 0 <= day and day <= 31:
            check_day =  True
        else:
            check_day =  False

        if 1 <= month and month <= 12:
            check_month =  True
        else:
            check_month =  False
        return check_day, check_month


my = Data("12-3-2020")
print(Data.data)
Data.parse_data()
print(Data.day)
print(Data.month)
print(Data.year)
check = Data.check_data(Data.day, Data.month)
print(check)

