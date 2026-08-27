import re

def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$|^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(pattern, ip):
        return True
    else:
        return False


ip = input("Enter IP address: ")

if validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")