try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except Exception as error:
    with open("error.txt", "a") as file:
        file.write(str(error) + "\n")

    print("An error occurred.")