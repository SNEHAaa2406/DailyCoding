import re

def signup(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+(\.[A-Za-z0-9]+)+\.[A-Za-z]{2,6}$'

    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Enter the email address: ")

if signup(email):
    print("Valid email address")
else:
    print("Invalid email address")