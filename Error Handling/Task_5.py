try:
    file = open("ridham.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    
    print("File not found.")

finally:
    
    print("File operation completed.")