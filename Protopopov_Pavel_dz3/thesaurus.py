"""
ЗАДАНИЕ:

3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имен,
а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:

>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
 в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
 в которых фамилия начинается с соответствующей буквы. Например:

>>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Сможете ли вы вернуть отсортированный по ключам словарь?
"""

names_list = ["Ivan", "Ira", "Arina", "Vasya", "Valera", "Varya", "Slava", "Kate", "Tom", "Tim"]
names_list_adv = ["Vera Orlova", "Ivan Popov", "Ira Kotova", "Arina Kukushkina", "Vasya Oblomov", "Valera Krotov", "Varya Postova", "Slava Rishov", "Kate Hill", "Tom Soyer", "Tim White", "Igor Balabanov", "John Akimov"]

def thesaurus(*names, sort = True):
    if sort == True :
        names = tuple(sorted(list(names)))
    letter_dict = {name[0]: [] for name in names}
    for name in names:
        letter_dict[name[0]].append(name)
    return letter_dict


def thesaurus_inn(*names, j, sort=True):
    if sort == True :
        names = tuple(sorted(list(names), key= lambda x: x.split()[j])) # ПЕРЕДЕЛАЛ ТЕПЕРЬ СОРТИРУЮТСЯ #names = tuple(sorted(list(names), key= lambda x: x.split()[j][0]))
    letter_dict = {name.split()[j][0]: [] for name in names}
    for name in names:
        letter_dict[name.split()[j][0]].append(name)

    return letter_dict

def thesaurus_adv(*names, sort=True):
    letter_dict = thesaurus_inn(*names, j= 1, sort=sort)
    for each in letter_dict:
        letter_dict[each] = thesaurus_inn(*letter_dict[each], j=0, sort=sort)
    return letter_dict

thesaurus_adv(*names_list_adv)

print("thesaurus:".upper())
print("names for thesaurus:     {}".format(names_list))
print("thesaurus is not sorted: {}".format(thesaurus(*names_list, sort = False)))
print("thesaurus is sorted:     {}".format(thesaurus(*names_list)))
print(" ")
print("thesaurus_adv:".upper())
print("names for thesaurus:     {}".format(names_list_adv))
print("thesaurus is not sorted: {}".format(thesaurus_adv(*names_list_adv, sort = False)))
print("thesaurus is sorted:     {}".format(thesaurus_adv(*names_list_adv)))
