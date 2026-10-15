numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    
    print("Invalid index. Index is out of range.")

except ValueError:
    print("Please enter a valid integer.")