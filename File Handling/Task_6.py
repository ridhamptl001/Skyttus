search_word = input("Enter the word forsearch: ")

with open("Ridham.txt", "r") as file:
    for line in file:
        if search_word.lower() in line.lower():
            print(line, end="")