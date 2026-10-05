strings = [
    "Ridham",
    "Working",
    "In",
    "Python",
    "Language"
     ]

with open("Ridham.txt", "a") as file:
    for text in strings:
        file.write(text + "\n")
print("Strings added successfully.")