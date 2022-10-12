from random import randint, randrange


n = int(input("enter length of list "))
my_list = []
new_list = []
index=0
for i in range(n):
    my_list.append(i)
print(my_list)
lenlist = len(my_list)
while lenlist != 0:
    index = randint(0,lenlist-1)
    new_list.append(my_list[index])
    my_list.pop(index)
    lenlist-=1
print(new_list) 