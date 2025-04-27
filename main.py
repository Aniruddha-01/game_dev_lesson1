list = ["apple","banana","orange","pineapple"]

for fruits in list:
    print(fruits)

list.append("apple")
list.append("banana")

fruit = input("Which fruit do you want? ")

count = 0
for fruits in list:
    if fruit == fruits:
        count += 1

print(count)

vitamins = {"apple": "C",
            "banana":"B",
             "pineapple":"K"}

print(vitamins[1])

tuple = ("mango","strawberry","banana","grape")

print(tuple[1:len(tuple)])