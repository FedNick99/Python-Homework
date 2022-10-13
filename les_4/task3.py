def fill_list(num):
    if type(num) != int or num <= 0:
        print("Negative value of the number of numbers!")
        exit()
    my_list = [input(f"enter elem # {i+1} : ") for i in range(num) ]
    return my_list

def diff_numb (my_list):
    if type(my_list) != list:
        return "Negative value of the number of numbers!"
    newlist = []
    my_dict = {}.fromkeys(my_list,0)
    for i in my_list:
        my_dict[i] += 1

    for j in my_dict:
        if my_dict[j] == 1:
            newlist.append(j)
    return newlist

print(diff_numb((fill_list(int(input("Enter a number of numbers : "))))))