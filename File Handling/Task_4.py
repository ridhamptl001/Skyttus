with open("Ridham.txt", "w") as file:

    for i in range(5):
        sentence = input("Enter a sentence: ")
        file.write(sentence + "\n")

print("5 sentences saved successfully.")