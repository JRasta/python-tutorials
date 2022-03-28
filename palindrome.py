a = input("Enter word/sequence: ")
a_lower = a.lower()
b = a_lower[::-1]
if a_lower == b:
    print("Palindrome")
else:
    print("Not a palindrome")
