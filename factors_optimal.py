from math import sqrt
num=36
result=[]
for i in range (1,int(sqrt(num)+1)):
    if num%i==0:
        result.append(i)
        if num//i !=i:       #here num//i !=0 sis because we printed till the sqrt number suppose till 6 but now for next numbers we have to          
            result.append(num//i)         #do num//i that is 36//1 will give 36 now 36//2 will give 18 but when it comes to 6 , 6 divide by 36 
result.sort()                             #gives 6 we cant repeat so we added !=i here.
print(result)