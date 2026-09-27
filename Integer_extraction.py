#Count the digits
text=int(input("Enter the digits:"))
count=0
while text>0:
    text = text// 10
    count+=1
print(count)