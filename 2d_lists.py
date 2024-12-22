
import random

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(matrix)




# print("number of rows " , len(matrix))
# print("number of cols " , len(matrix[0]))
# print("number of cols " , len(matrix[1]))
# print("number of cols " , len(matrix[2]))


# for i in range(len(matrix)):
#     for j in range (len(matrix[i])):
#         print(matrix[i][j] , end=" ")
#     print()




# # Get 20 random marks for 20 students (between 0 to 100). Create 3 separate lists . The first list should contain the marks <=30. The second list between 31 to 69. The third list >= 70.
# # Display the output lists

list1 = []
list2 = []
list3 = []
list_of_marks = []
for i in range(20):
    list_of_marks.append(random.randint(0,100))

for i in list_of_marks:
    if i <= 30:
        list1.append(i)
    elif i > 31 and i <= 69:
        list2.append(i)
    else:
        list3.append(i)


print(list1)
print(list2)
print(list3) 



