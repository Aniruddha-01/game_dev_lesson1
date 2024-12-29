

list = ['Ani', 'Rishaan', 'Aadil']
print(list)
while(True)
    print('This is the current list', list)
    operation = int(input('Chose one of the following : 1. Add a name to the list, 2.Change a name in the list, 3.Delete a name from the list, 4.View all names from the list '))

    if operation == 1:
        element = input('What do you want to add ')
        list.append(element)
        print('This is the current list', list)

    elif operation == 2:
        index = int(input('Enter the index of the name you want to change '))
        new_name = input('Enter the new name ')
        list[index]=new_name
        print('This is the updated list', list)

    elif operation == 3:
        delete_name = ('Enter the name you want to delete ')
        list.remove(delete_name)

    elif operation == 4:
        for i in list:
            print(i)

    elif operation == 5:
        break
    else:
        print('Please choose a valid input')