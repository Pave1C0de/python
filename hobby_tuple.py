"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом —
данные об их хобби. Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи

4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа.
Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.

5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам
и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
"""

# В данном задании использовать ФИО в качестве ключа словаря достаточно опасно, если придется добавить
# двух полных тесок. Это будет проблема. Поэтому необходимо вводить какой-нибудь искусственный счетчик полных
# тесок. Особенно, если рассчитывать, что размер списка будет больше размера оперативной памяти


def make_tuple(src_adress, res_adress):
    try:
        names_csv   = "users.csv"
        hobbies_csv = "hobby.csv"
        result_csv  = "result.csv"
        src_adress1 = src_adress + names_csv
        src_adress2 = src_adress + hobbies_csv
        res_adress  = res_adress + result_csv
        #tuple_ret   = {}
        # открываем 2 файла на чтение и один на запись
        with open(src_adress2, 'r', encoding='utf-8') as f2:
            with open(src_adress1, 'r', encoding='utf-8') as f1:
                with open(res_adress, 'w', encoding='utf-8') as f3:
                    for line1 in f1:
                        l2 = f2.readline()
                        if l2:
                            # если размер файлов больше размера ОЗУ нельзя все складывать в tuple,
                            # нужно писать сразу в файл, в ПЗУ на HDD
                            # но если так нужно, то этот код я закомментировал:

                            #tuple_ret[tuple(line1.strip("\n").split(","))] = l2.strip("\n").split(",")
                            f3.write(line1.strip("\n") + " : " + l2.strip("\n") + "\n")
                        else:
                            #tuple_ret[tuple(line1.split(","))] = None
                            f3.write(line1.strip("\n") + " : " + "None\n")
                        #f3.write(str(list(tuple_ret.keys())[-1]) + " : " + str(list(tuple_ret.values())[-1]) + "\n")
            if f2.readline():
                return 1
            else:
                return 0
            #    return tuple_ret
    except FileNotFoundError:
        print("Can't find source file. Please check it")
        return -2


#result = make_tuple("users.csv", "hobby.csv", "result.csv")
#print(result)


def main(argv):
   program, *arg = argv
   try:
        result = make_tuple(arg[0], arg[1])
        #print(f'результат: {result}')
        return result
   except:                                      # if no args
       print("VALUE ERROR:\nthis c0de get two arguments valute code! Please enter valute code")
       print("\nCOMMAND FORMAT:\npython hobby_tuple.py src_adr//src_adr//..// res_adr//res_adr//..//")
       print("\nFILES FORMAT:\nsrc_files: users.csv, hobby.csv \nres_files: result.csv")
       return -1



if __name__ == '__main__':
   import sys

   exit(main(sys.argv[:3]))


