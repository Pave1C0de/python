"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно);
 предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

import os

def parce_yaml_line(line):
    l = ''
    for i in line:
        l = l + (" " + str(ord(i)))
    layer = int(l.count("32 ")/4)

    if line[-2 : ] == ":\n":
        df = line[layer * 4 : -2]
        mode = "d"
    else:
        df = line[layer * 4 : -1]
        mode = "f"
    #print(layer, df, mode, sep="____")
    return layer, df, mode


configure_file = 'config.yml'
try:
    with open(configure_file, 'r', encoding='utf-8') as file_1:
       layer = 0
       old_layer = 0
       adr = ""
       for line in file_1:
           layer, string, mode = parce_yaml_line(line)

           if mode == "d":                                  #d - directory mode line
               if layer < old_layer:
                   adr = os.path.join(*adr.split("\\")[: (old_layer - layer -1)])
               elif layer == old_layer:
                   adr = os.path.join(*(adr.split("\\")[: -1]))
               # if layer > old_layer and all others cases:
               adr = os.path.join(adr, string)
               old_layer = layer
               # create directory:
               if not os.path.exists(adr):
                   os.mkdir(adr)
               # print(adr, layer, old_layer, sep="____")


           elif mode == "f":                                 #f - file mode line
               file = os.path.join(adr, string)
               # create file:
               with open(file, 'w', encoding='utf-8') as file_1:
                   pass
               #print(file, layer, old_layer, sep="____")
except (FileNotFoundError, EOFError) as e:
    print(f"File {configure_file} can't found: {e}")


