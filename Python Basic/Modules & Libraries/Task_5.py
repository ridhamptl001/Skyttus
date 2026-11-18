import math

num=int(input("Enter a number:"))

if num<0:
    print("factorial is not defined for negative numbers")
else:
    result=math.factorial(num)
    print("factorial:",result)