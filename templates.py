"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
"""

import os
from os.path import relpath

root_dir    = r'my_project' #dir for find
choise_dir  = r'templates'  #dir for group created dirs

find_dirs = []
for root, dirs, files in os.walk(root_dir):
   for file in files:
       rel_path = relpath(os.path.join(root, file), root_dir)
       if choise_dir in rel_path:
           path = os.path.join(root_dir, choise_dir) + rel_path.split(choise_dir)[1]
           try:
               if not os.path.exists(os.path.dirname(path)):
                   os.makedirs(os.path.dirname(path))
               with open(path, 'w', encoding='utf-8') as file_1:
                   pass
           except:
               print(f"Some thing wrong with create directory or file. Please check it: {path}")
