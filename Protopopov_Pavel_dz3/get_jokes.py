"""
ЗАДАНИЕ:

5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(jokes_num, nouns=nouns, adverbs=adverbs, adjectives=adjectives, all_new_jokes=False):
    """
    :param jokes_num:       <int> - nums of jokes
    :param nouns:           <list> - list nouns for jokes
    :param adverbs:         <list> - list adverbs for jokes
    :param adjectives:      <list> - list of adjectives for jokes
    :param all_new_jokes:   <bool> - func will be generate jokes from new words
    :return:                <list> - list of jokes but None if wrong jokes_num
    """
    jokes = list()
    if isinstance(jokes_num, int):
        if all_new_jokes == False:
            for i in range(jokes_num):
                jokes.append(random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives))
        elif (jokes_num > min(len(nouns), len(adverbs), len(adjectives))) and (all_new_jokes == True) :
            return None
        elif (jokes_num <= min(len(nouns), len(adverbs), len(adjectives))) and (all_new_jokes == True) :
            shuffled = list(range(jokes_num))
            random.shuffle(shuffled)
            for i in shuffled:
                jokes.append(nouns[i]+" "+adverbs[i]+" "+adjectives[i])
        return jokes
    else:
        raise TypeError("Wrong input type")


print("jokes_num value is doesn't matter 'all_new_jokes=False' : {}".format(get_jokes(6)))
print("jokes_num more then can be with 'all_new_jokes=True'    : {}".format(get_jokes(4, all_new_jokes=True)))
print("jokes_num in correct range and 'all_new_jokes=True'     : {}".format(get_jokes(6, all_new_jokes=True)))
get_jokes(6.3)