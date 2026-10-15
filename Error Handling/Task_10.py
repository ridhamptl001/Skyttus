class Email(Exception):
    pass
try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise Email("Invalid email format.")

    print("Valid email.")

except Email as error:
    print("Error:", error)