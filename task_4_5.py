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
######################__TEST__###########################
# for test ask in terminal next:
#    python task_4_5.py USD
#    python task_4_5.py usd
#    python task_4_5.py 840
#    python task_4_5.py 36
#    python task_4_5.py 27
#########################################################
def ask_for_test():
    print("######################__TEST__###########################")
    print("  for test ask in terminal next:")
    print("     python task_4_5.py USD")
    print("     python task_4_5.py usd")
    print("     python task_4_5.py 840")
    print("     python task_4_5.py 36")
    print("     python task_4_5.py 036")
    print("     python task_4_5.py 27")
    print("     python task_4_5.py USV")
    print("#########################################################")
def main(argv):
   program, *arg = argv
   try:
        if (arg[0].lower() == "help") or (arg[0].lower() == "h"):
            ask_for_test()
            return 0
        else:
            result = Utils.currency_rates(arg[0])
            print(f'результат: {result[0]}, {result[1]}')
            return 0
   except:                                      # if no args
       print("VALUE ERROR: this c0de get one argument valute code! Please enter valute code")
       print("for HELP ask in terminal next: python task_4_5.py help")
       return -1



if __name__ == '__main__':
   import sys
   import Utils

   exit(main(sys.argv[:2]))
