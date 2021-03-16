"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...

2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
#import itertools
def odd_nums(max_num):
   for num in range(1, max_num + 1, 2):
       yield num

num = odd_nums(13)
print(type(num))
for i in range(0, 7):
    print(next(num))

max_num  = 13
nums_gen = (num for num in range(1, max_num + 1, 2))
print(*nums_gen)
