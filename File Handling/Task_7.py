oldword = input("Enter word to replace: ")
newword = input("Enter new word: ")

with open("Ridham.txt", "r") as file:
    content = file.read()

content = content.replace(oldword, newword)
with open("Ridham.txt", "w") as file:
    file.write(content)


print("Word replaced successfully.")