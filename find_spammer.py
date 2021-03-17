"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
превышает объем ОЗУ компьютера.
"""

from requests import get, utils


#################################################################################################
# Как читаль контент из URL построчно (Это возможно)? Или кусками меньше, чем размер RAM? Иначе все теряет смысл
# Или нужно загружать файл txt сразу на HDD, а потом читать построчно?
#################################################################################################

def https_to_txt(url_adr, txt_file):
    """
    This function get access to http resource (url_adr) Convert content of resourse to txt format (txt_file) current project :
    :param url_adr:     adress for get content      (str)
    :param txt_file:    text file for save content  (str)
    :return:            0 (int) - if success open url adress (url_adr) and create result file (txt_file)
                       -1 (int) - if can't open url adress
                       -2 (int) - if can't create result file (txt_file)
    """
    try:
        response = get(url_adr)
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
    except:
        print("ERROR: 'https_to_txt' function is crushed. Function can't get access to http resource: \n {}".format(url_adr))
        return -1
    try:
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.writelines(content)
        return 0
    except IOError:
        print("ERROR: 'https_to_txt' function is crushed can't open file {}".format(txt_file))
        return -2


def line_parse(line):
    """
    This function get one line from file and return it to next format: (<remote_addr>, <request_type>, <requested_resource>)
    :param line:    (str)   line for parse
    :return:        (tuple) <remote_addr>, <request_type>, <requested_resource> - from line
    """
    remote_addr = line.split(" - - ")[0]
    request_type = line.split(" - - ")[1].split('"')[1].split()[0]
    requested_resource = line.split(" - - ")[1].split('"')[1].split()[1]
    return remote_addr, request_type, requested_resource


def spammer_detect(line, spammer_requests):
    """
    This function fill dictionary key is ip-adress and value is quantity of requests
    :param line:             (str) parsed string from src file format :
                             <remote_addr>, <request_type>, <requested_resource>
    :param spammer_requests: (dict) empty dictionary for filling
    :return:                 spammer_requests implicit
    """
    ip = line.split()[0][1:-2]
    if ip in spammer_requests:
        spammer_requests[ip] += 1
    else:
        spammer_requests.update({ip:1})


# На случай, если нужно найти спамера по файлу
def spammer_detect_after_parse(parse_log_f):
    try:
        with open(parse_log_f, 'r', encoding='utf-8') as f:
            spammer_requests = {}
            for line in f:
                ip = line.split()[0][1:-2]
                if ip in spammer_requests:
                    spammer_requests[ip] += 1
                else:
                    spammer_requests.update({ip:1})
        print("SPAMMER DETECTED: {}, (requests quantity: {})".format(
            sorted(spammer_requests.items(), key=lambda x: x[1])[-1][0],
            sorted(spammer_requests.items(), key=lambda x: x[1])[-1][1]))
        return 0
    except IOError:
        return -2


def log_parse(log_f, parse_log_f):
    """
    This function open txt file with logs, read it line by line and write in format line_parse of function to parse_log_f txt file
    :param log_f:           resource txt file
    :param parse_log_f:     txt file wich will be create. There will be write result of parse
    :return:                0 (int) - function right work
                           -2 (int) - something goes wrong with files log_f or parse_log_f
    """
    try:
        spammer_requests = {}
        ip  = 0
        req = 1
        # открываем 2 файла иии давай один по строчке разбирать, а в другой записывать !
        with open(log_f, 'r', encoding='utf-8') as f:
                with open(parse_log_f, 'w+', encoding='utf-8') as f1:
                    for line in f:
                        line_free_brackets = str(line_parse(line))[1:-1]
                        # записываем обработанную строку в файл
                        f1.write(line_free_brackets+"\n")

                        # находим спамера сразу при чтении по строкам, чтобы не читать файл повторно
                        spammer_detect(line_free_brackets, spammer_requests)
                    #сортируем dict по value(счетчику) и берем максимальное значение => spammer
                    spammer = sorted(spammer_requests.items(), key=lambda x: x[1])[-1]
                    print("SPAMMER DETECTED: {}, (requests quantity: {})".format(spammer[ip], spammer[req]))
        return 0
    except IOError:
        return -2



url         = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs" # src url
txt_f       = "nginx_logs.txt"                                                                               # src file
parse_log_f = "tuples_list.txt"                                                                              # rsult file

https_to_txt(url, txt_f)
log_parse(txt_f, parse_log_f)

