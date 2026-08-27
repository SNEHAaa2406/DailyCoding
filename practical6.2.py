# 14.	Write a program to build a password strength checker for a website that ensures users create secure passwords. Write a function that:
# ●	Accepts a password string as input.
# ●	Uses regular expressions to check if the password meets the following criteria:
# o	At least 8 characters long.
# o	Contains at least one uppercase letter.
# o	Contains at least one lowercase letter.
# o	Contains at least one digit.
# o	Contains at least one special character (!@#$%^&*()-_).
# ●	Return True if the password is strong and False if it fails any criteria.
# Tasks:
# ●	Use regular expressions to validate the strength of the password based on the given rules.

import re

def check_password(password):

    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_-]).{8,}$'

    if re.match(pattern, password):
        return True
    else:
        return False


password = input("Enter password: ")

if check_password(password):
    print("Strong password")
else:
    print("Weak password")
