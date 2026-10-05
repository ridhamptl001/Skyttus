def check_palindrome(word):
    
    
    if word == word[::-1]:
        return True
    else:
        return False
text = input("Enter a word: ")
if check_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")