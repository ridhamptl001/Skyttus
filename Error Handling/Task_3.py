try:
    with open("ridham.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")