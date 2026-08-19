word = input("Enter a word: ")
letters = {}
for ch in word:
    letters[ch] = letters.get(ch, 0) + 1
print(letters)