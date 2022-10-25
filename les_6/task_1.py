# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
from random import randint
def fill_list(num:int) -> list:
    if type(num) != int or num <= 0:
        print("Negative value of the number of numbers!")
        exit()
    my_list = [randint(0,20) for i in range(num)]
    return my_list

my_list = fill_list(int(input("Enter a number of numbers ")))
print(my_list)
my_list = [print(my_list[i], end=' ') for i in range(len(my_list)) if my_list[i]>my_list[i-1]]



