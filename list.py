"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""
class NotNumberExcept(Exception):
    def __init__(self, text):
        self.txt = text

my_list = list()
while True:
    number = input("Введите число:")
    if type(number) == str and number.lower() == "q" or number.lower() == "quit":
        break
    try:
        if (number.lower() != "q" or number.lower() != "quit") and not(number.isdigit()):
            raise NotNumberExcept("ERROR: Это не число! Повторите попытку")
        else:
            my_list.append(number)
    except NotNumberExcept as err:
        print(err)

print(my_list)
