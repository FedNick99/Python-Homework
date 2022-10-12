num_of_elems = int(input("enter number of elements "))
num_1 = int(input('enter num_1 '))
num_2 = int(input("enter num_2 "))
my_list = []
if ((num_1 or num_2) > num_of_elems*2+1) or ((num_1 or num_2) <= 0):
     print("positions are out of range")
else:
    for i in range(-num_of_elems,num_of_elems+1):
        my_list.append(i)
    result_sum = my_list[num_1-1]*my_list[num_2-1]
    print(result_sum)
    print(my_list)
