from winreg import REG_RESOURCE_REQUIREMENTS_LIST


n = int(input("enter number "))
result_sum =0
my_list = []
for i in range(1,n+1):
    my_list.append(round((1+1/i)**i))
    result_sum += my_list[i-1]
print(my_list)
print(result_sum)