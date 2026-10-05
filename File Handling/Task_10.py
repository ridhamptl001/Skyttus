with open("Ridham.txt", "r") as original:
    content = original.read()

with open("data_backup.txt", "w") as backup:
    backup.write(content)
print("Backup created successfully.")