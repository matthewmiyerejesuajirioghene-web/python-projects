number = input("Enter in your number: ")
digits_analyze = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "0": "Zero"
}
output = ""
for ch in number:
    output += digits_analyze.get(ch, "!!") + " "
print(output)