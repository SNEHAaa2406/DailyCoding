num=121
n=num
result=0
while num>0:
    id=num%10
    result=(result*10)+id
    num=num//10
if result==n:
    print("yes")
else:
    print("no")