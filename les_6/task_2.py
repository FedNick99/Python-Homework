# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
def fill_list(num:int) -> list:
    if type(num) != int or num <= 20:
        print("Negative value of the number of numbers!")
        exit()
    my_list = [i for i in range(20,num+1) if i%20 == 0 or i%21==0]
    return my_list
print(fill_list(int(input("Enter n (n>20) "))))