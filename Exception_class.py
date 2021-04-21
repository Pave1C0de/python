"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyCustomError(Exception):
    def __init__(self, text):
        self.txt = text

try:
    inp_data = input("Введите 'делимое/делитель': ")
    inp_data = inp_data.split("/")
    divisible = int(inp_data[0])
    divisor = int(inp_data[1])
    if divisor == 0:
        raise MyCustomError("Деление на ноль")
    else:
        result = divisible / divisor
        print(f"Результат деления: {result}")
except MyCustomError as err:
    print(err)
else:
    pass
