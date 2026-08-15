# 16.	Character Frequency 
# a.	Display the frequency of every character in a string. 
sen = input("Enter a string: ")

freq = {}

for i in sen:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)