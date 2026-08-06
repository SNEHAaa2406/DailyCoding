# num=list(map(int,input("Enter elements:").split()))
# print(num)

# Here split() used to split the string wherver there is a space 
# int to take all strings as integer
# and map(int,...) used to convert every string into an integer. 
# list (...) stores them in the list.
# ------------------------------------------------------------------------

#  Enter elements one by one 
# arr=[]
# for i in range(5):
#     num=int(input(f"Enter integer {i+1}: "))
#     arr.append(num)
# print(arr)


# f-string also called as formatted string
# here f lets you put a variable inside a string
# suppose without f ,
            #  num=int(input("enter elements {i+1}"))
            # then it will display :
            # enter elements {i+1}

# {} whatever inside this curly bracket replaces with it's value ,
# suppose , 
            #   age=20
            # print(f"age is {age}")
        # output will be : 
            #    age is 20

# ---------------------------------------------------------------------------------------
# Now the final quetsion ,
# Q1. Enter 5 elements in an array and access all by indexing 

# arr=[]
# for i in range(5):
#     num=int(input(f"Enter integer {i+1} :"))
#     arr.append(num)
# print(arr)

# a=int(input("Enter the index of number you want :"))
# print(arr[a])
# ----------------------------------------------------------
# Q2. Add the element in the end of an array

# arr=[12,54,80]
# print("Original list is :",arr)
# a=int(input("Enter the number you want to add :"))
# arr.append(a)
# print(arr)
# ----------------------------------------------------------------
# Q3. Reverse order of items in an array
# arr=[45,87,69,20]
# print(arr)
# -----------OR-----------
# arr=[45,87,98,51] 
# reverse=arr[::-1]
# print(reverse)