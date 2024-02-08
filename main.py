
"""1) Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая 
строка должна быть пронумерована.

2) Напишите функцию, которая принимает список, из списка выдает 
случайное значение из списка и записывает результат в txt файл. 
Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

3)names = [“azat”, “zina”, “kuma”, “anna”, “sas”] 
Вывести с помощью lambda функции имена палиндромы"""

# 1
def func():
    for word in range(1,6):
        print(f"{word}: 0")
func()

# 2
import random

language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

word_random = random.choice(language)

with open('result.txt', 'w') as write_file:
    write_file.write(word_random)
with open('result.txt', 'r') as write_read:
    write_read.read()

# 3

names = ["azat", "zina", "kuma", "anna", "sas"]
name_pol = list(filter(lambda x: x == x[::-1], names))
print(name_pol)

