from unittest import result


numb = float(input("enter float number "))
line_1 = str(numb)
step = len(line_1[line_1.find("."):])
numb = int(numb*10**(step-1))
result = 0
while numb!=0 :
    result += numb%10
    numb = numb//10
print(result)
