text = input("Enter a word: ")

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count += 1

print("Vowels:", count)