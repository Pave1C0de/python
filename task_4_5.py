"""
ЗАДАНИЕ:
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

> python task_4_5.py USD
75.18, 2020-09-05

"""

"""
276 - цифровой код валюты; DEM - буквенный код валюты; Немецкая марка - наименование валюты; 
"""




def main(argv):
   program, *arg = argv
   try:
        result = Utils.currency_rates(arg[0])
        print(f'результат: {result[0]}, {result[1]}')
        return 0
   except:                                      # if no args
       print("VALUE ERROR: this c0de get one argument valute code! Please enter valute code")
       return -1



if __name__ == '__main__':
   import sys
   import Utils

   exit(main(sys.argv[:2]))