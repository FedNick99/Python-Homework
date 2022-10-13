from decimal import Decimal
def num_accurancy(num,accurancy):
    num = Decimal(num)
    return num.quantize(Decimal(accurancy))


print(num_accurancy(input("Enter a real number: "),input("Enter the required accuracy '0.0001': ")))