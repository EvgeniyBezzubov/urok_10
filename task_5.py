"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import chardet
import os
import subprocess
ping = "ping "
web = ["yandex.ru", "youtube.com", "gb.ru"]
for i in web:
    command = ping + i
    print(command)
    YA_PING = subprocess.Popen(command, stdout = subprocess.PIPE)
    print(YA_PING.stdout)
    for line in YA_PING.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))
    print(os.name)
