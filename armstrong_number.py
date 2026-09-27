digit=153
n=digit
total=0
nod=len(str(digit))
while digit>0:
    id=digit%10
    total+=id**nod
    digit=digit//10
if (n==total):
    print("It is a armstrong number")
else:
    print("Not a armstrong number")