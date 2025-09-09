# password_checker.py
password = input("Enter a password to check strength: ")

if len(password) < 6:
    print("Weak password")
elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Moderate password")
else:
    print("Strong password")
