# # Sets store data which is unique

# list = ("apple","banana","banana","cherry")
# print(list)

# sample_set = set(list)
# print(sample_set)

# # sets are not indexable
# # print(sample_set[1])

# # check if an element is present in the set
# if "banana" in sample_set:
#     print("yes")
# else:
#     print("no")

# # To add things to a set: add function ---> adds data to start
# sample_set.add("blueberry")
# print(sample_set)

# # Removeing an element: remove function
# sample_set.remove("apple")
# print(sample_set)

# # discard function: remove from the set
# sample_set.discard("blueberry")
# print(sample_set)

# # Operations on a set
# a = {1,2,3,4}
# b = {2,5,6,7,8}

# # Union
# union_set = a.union(b)
# print("union",union_set)

# # Intersection
# intersection_set = a.intersection(b)
# print("intersection",intersection_set)

# # Difference
# difference_set = a-b
# print("difference", difference_set)


# # Symetrice difference: Everything but the intesection
# sym_diff = a.symmetric_difference(b)
# print("sym_diff", sym_diff)


og_sentence = {"Python","is","fun","and","Python","is","powerful"}
sentence_set = set(og_sentence)
print(sentence_set)