# 1.	Count Occurrences of a Word 
# a.	Count how many times a specific word appears in a sentence. 

sen="Hiii I'm sneha here ? sneha saying hello to you"
word=input("Enter the specific word :")
count=sen.count(word)
if count==0:
    print("No word found")
else:
    print(count,"times it appeared")