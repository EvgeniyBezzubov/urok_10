"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["разработка", "администрирование", "protocol", "standard"]
for i in words:
    word = i.encode('utf-8')
    print(word, "после метода encode")
    print(word.decode('utf-8'), "после метода decode")

