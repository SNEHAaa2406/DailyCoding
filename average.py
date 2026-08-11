arr = [10, 20, 30, 40]

num = int(input("Enter number: "))

found = False

for i in arr:
    if i == num:
        found = True

if found:
    print("Found")
else:
    print("Not Found")