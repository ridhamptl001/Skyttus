try:
    num1=int(input("Enter the number 1:"))
    num2=int(input("Enter the number 2:"))
    
    result=num1/num2
    print("the result is:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")