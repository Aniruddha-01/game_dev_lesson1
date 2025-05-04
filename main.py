
names = []
flag = False
while True:
    option = int(input('You can add (1), change (2) remove(3) and view(4) names in this list. Type the number corresponding to the option you want to pick. To stop the program, press 5. '))

    if option == 1:
        add_name = input('Enter the name you want to add to the list ')
        names.append(add_name)

    elif option == 2:
        change_name = input('Enter the name you want to change ')
        for i in range(len(names)):
            if names[i] == change_name:
                flag = True
                names[i] = input('Enter the new name to replace the old name ')
                break 
            if flag == False:
                print('Name not found ')
    
    elif option == 3:
        remove_name = input('Enter the name you want to remove ')
        names.remove(remove_name)
    
    elif option == 4:
        for name in names:
            print(name)

    elif option == 5:
        break 
            
    
    