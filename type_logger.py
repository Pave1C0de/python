"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

>>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:

>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

def p_wrapper(func):

   def tag_wrapper(*args, **kwargs):
       print("function: ", str(func).split()[1])
       if args:
           for i in args:
               print(i, str(type(i)).split("'")[1], sep=" type ")
       if kwargs:
           for j in kwargs:
               print(j, str(type(j)).split("'")[1], sep=" type ")
       ret = func(*args, **kwargs)
       print(f'return type of function: {str(type(ret)).split()[1]}')
   return tag_wrapper

@p_wrapper
def render_input(field):
   return f'<input id="id_{field}" type="text" name="{field}">'


@p_wrapper
def power2(*item):
    try:
        f = [int(i)**2 for i in item]
        return f
    except:
        return -1

ff = power2(3, "34", 4)
print(ff)

ff = power2(3, "34", 4, "55", 0.34, "0.003")
print(ff)

username_f = render_input(field='username')
print(username_f)

