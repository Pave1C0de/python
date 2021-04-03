"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""


import os
from os.path import relpath
import json

target_folder_direct_path = r"C:\Users\__\__\GeekBrains\__\lessons\lesson_7\pythonProject1" #set your path
my_dict = {}

for root, dirs, files in os.walk(target_folder_direct_path):
   for file in files:
       rel_path = relpath(os.path.join(root, file))
       i = 1
       while os.stat(rel_path).st_size // (10**i) >= 1: i += 1
       if my_dict.get(10**i) == None:
           my_dict[10**i] = [1, [os.path.basename(rel_path).split(".")[-1]]]
       else:
           my_dict[10**i][0] += 1
           if not(rel_path.split(".")[-1] in my_dict[10**i][1]):
               my_dict[10 ** i][1].append(os.path.basename(rel_path).split(".")[-1])

with open('nums_again.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f)
