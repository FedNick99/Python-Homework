from decimal import Decimal

num = Decimal(input("Enter a real number : "))
accurancy = input("Enter the required accuracy '0.0001'")
print(num.quantize(Decimal(accurancy)))
