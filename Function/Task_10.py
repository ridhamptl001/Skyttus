def armstrong(number):
    original = number
    digits = len(str(number))
    total = 0


    while number > 0:
        digit = number % 10
        total = total + digit ** digits
        number = number // 10
    return total == original



num = int(input("Enter a number: "))
if armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")