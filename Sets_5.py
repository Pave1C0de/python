"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_non_recurring = [el for el in src if src.count(el) == 1] # не очень хорошее решение с count()
print(src_non_recurring)


result = list()
full_set = set(src)
for el in src:
    src_cpy = src.copy()
    src_cpy.remove(el)
    cmp_set = set(src_cpy)
    if full_set != cmp_set:
        result.append(el)
print(result)

