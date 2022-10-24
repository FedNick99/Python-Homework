# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел
from random import sample

def fill_list (count:int = 0,abc:str = "абв") -> str:
    new_list = ["".join(sample(abc,len(abc))) for i in range(count)]
    return " ".join(new_list)


def del_abc (word_list:str) -> str:
    return " ".join(word_list.replace("абв","").split())

new_list = fill_list(int(input("Enter number of words")))
print(new_list)
print(del_abc(new_list))