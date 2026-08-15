# Problem 4 — List + counting
# Take 5 integers from the user.
# Count how many numbers are even

# My wrong solution 
# count=0
# arr=list(map(int,input("Enter 5 elements:").split()))
# if len(arr)==5:
#     print(arr)
# else:
#     print("Enter only 5 elements.")
# for i in range(0,5):
#      if arr[i]%2==0:
#         count+=1
#         print(count,"are total even numbers")
#      else:
#         print("No even numbers")
    
# correct solution
count = 0

arr = list(map(int, input("Enter 5 elements: ").split()))

if len(arr) == 5:
    for i in range(5):
        if arr[i] % 2 == 0:
            count += 1

    print(count, "are total even numbers")
else:
    print("Enter only 5 elements.")