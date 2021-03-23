"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError. Пример:

>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?

"""

import re

def email_parse(email_address):

     pattern_1 = re.compile(r'^\w+[\w\d\.]+@(?:[a-zA-Z])+\.+[a-zA-Z]{2,4}$')
     if pattern_1.match(email_address):
          return {'username': email_address.split("@")[0], 'domain' : email_address.split("@")[1]}
     else:
          raise ValueError(f"Wrong email adress: {email_address}")
          return -1
email_parse('hgh.jk@yandex.ru')
email_parse('hgh.jk@yan.dex.ru')



