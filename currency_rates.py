"""
ЗАДАНИЕ:
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно
запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str,
решить поставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте:
есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется
код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции?
"""

"""
276 - цифровой код валюты; DEM - буквенный код валюты; Немецкая марка - наименование валюты; 
"""
from datetime import datetime
import requests


def in_valute_find_tag_val(in_valute, content, tag):
    """
    :param in_valute: (str type) (<CharCode> or <NumeCode>) + value
    :param content:    (html page code)
    :param tag: "<Nominal>" or "<Value>"
    :return: return value between tag from html (str)
    """
    val_start = in_valute + content[in_valute:].find(tag) + len(tag)    # value start
    val_stop  = in_valute + content[in_valute:].find("</" + tag[1:])    # value stop
    return content[val_start : val_stop]


def currency_rates(money_code, url = 'http://www.cbr.ru/scripts/XML_daily.asp'):
    """
    function for get exchange rate relative to the ruble.
    Data comes from url 'http://www.cbr.ru/scripts/XML_daily.asp',
    but you can change it if format urls same. For this function need import
    requests and datatime libs

    :param money_code: letter(str type) or number(int type) code of currency.
    :param url: url(str type) for get data. You can change it if format your URL same
    :return: tuple format: (exchange rate(float), data(datatime.data))
    """
    response = requests.get(url)                                        # set url for requests
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    Date = response.headers.get("Date").split()                         # get request data from server
    date_str = Date[1] + "-" + Date[2] + "-" + Date[3]
    dashed_format = '%d-%b-%Y'
    parsed_date = datetime.strptime(date_str, dashed_format)            #
    return_data = parsed_date.date()
    response.close()
    if      isinstance(money_code, int):
        str_money_code = "{:03}".format(money_code)
        in_valute = content.find("<NumCode>" + str_money_code)          # Valute pointer
    elif    isinstance(money_code, str):
        str_money_code = money_code.upper()
        in_valute = content.find("<CharCode>" + str_money_code)         # Valute pointer
    else :
        return None, return_data
    if in_valute == -1 :
        return None, return_data
    nominal = in_valute_find_tag_val(in_valute, content, "<Nominal>")
    Value = in_valute_find_tag_val(in_valute, content, "<Value>")
    valute_unit_in_rubles = round(float(Value.replace(",","."))/int(nominal), 2)
    return valute_unit_in_rubles, return_data

print("USD:         {} {} {}".format(currency_rates("usd")[0], currency_rates("USD")[0], currency_rates(840)[0]))
print("EUR:         {} {} {}".format(currency_rates("eur")[0], currency_rates("EUR")[0], currency_rates(978)[0]))
print("None case:   {} {} {}".format(currency_rates(1)[0], currency_rates(["eur", "usd"])[0], currency_rates("eru")[0]))
print(str(currency_rates("usd")[1]))
