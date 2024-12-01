#count the occurence of vowels in the string entered by the user

str = input("Enter a string")

# vowels = {
#     "a" : 0
#     "e" : 0
#     "i" : 0
#     "o" : 0
#     "u" : 0
# }

# for storeChar in str:
#     storeChar.lower()
#     if Char in vowels:
#         vowels[Char]+=1

# print(vowels)

#Count the occurence of each alphabet in the string entered by the use


charCount = {}

for c in str:
    if c.isalpha():
        c = c.lower()
        if c in charCount:
            charCount[c] += 1
        else :
            charCount[c] = 1

print(charCount)
