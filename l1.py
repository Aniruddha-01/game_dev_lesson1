# #dictionaries 
# #Key : Value
names = {
"Aniruddha" : "blue"  ,
"Rishaan" : "Green"  ,
"Atharva" : "Red"   ,
"Yash"  :  "Yellow" ,
"Aarush" : "black"  ,
}
# print(names)
# #Access elements from the dictionary
# print(names["Aniruddha"])
# print(names["Rishaan"])
# print(names["Atharva"])

# #Updating a value
# names["Aniruddha"] = "black"
# names["Aarush"] = "blue"

# print(names)

# #Adding elements to the list
# names["Ani"] = "orange"
# print(names)

# #delete elements

# del names ["Ani"]
# print(names)

if "Aniruddha" in names:
    print("Aniruddha is in the dictionary with the value", names["Aniruddha"])
else:
    print("Aniruddha is not in the dictionary")

#length of the dictionary
print(len(names))
