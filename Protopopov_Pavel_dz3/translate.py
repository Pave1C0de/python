"""
ЗАДАНИЕ:

1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:

>>> >>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:

>>> >>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""
my_dictionary = {
    "one" : "один",
    "two" : "два",
    "three" : "три",
    "four" : "четыре",
    "five" : "пять",
    "six" : "шесть",
    "seven" : "семь",
    "eight" : "восемь",
    "nine" : "девять",
    "ten" : "десять"
    }

def num_translate_adv(word, dictionary = my_dictionary):
    """
    :param word: <str> word for translate
    :param dictionary: <dict> default is my_dictionary
    :return: translated word or None if word is not in dictionary, also can raise error
    """
    if isinstance(word, str) and isinstance(dictionary, dict):
        dict_word = word.lower().strip()            # lower word with remove space for check in dictionary
        if dict_word in my_dictionary:
            if word.isupper():
                return dictionary[dict_word].upper()
            elif word.istitle():
                return dictionary[dict_word].title()
            else:
                return dictionary[dict_word]
        else:
            return None
    else:
        raise TypeError(" please check arguments types of function  num_translate() ")


# TEST:
print("{:<8} --> {:<10}".format("word", "translate"))
print("-"*20)
for i in my_dictionary:
    print("{:<8} --> {:<10}".format(i, num_translate_adv(i, my_dictionary)))

words = ["fox", "One", "ONE", " seven ", 12]
for i in words:
    print("{:<8} --> {}".format(i, num_translate_adv(i, my_dictionary)))



