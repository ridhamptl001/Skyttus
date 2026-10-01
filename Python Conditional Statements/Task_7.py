username="Ridhamptl"
password="Ridhamptl@123"

username_input=input("Enter your username:")
password_input=input("Enter your password:")

if username_input != username:
    print("Invalid username.")
elif password_input != password:
    print("Invalid password.")
else:
    print("Login successful.")