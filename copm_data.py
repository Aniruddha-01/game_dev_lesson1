
group_num = 1
for i in range(5):
    print('Group',group_num)
    group_name = input('Enter the name of your group ')
    group_size = input('Enter the size of your group ')
    comp_date = input('Enter the date of the competition in DD-MM-YYYY ')
    medal_type = input('Enter the type of medal recieved ')
    group= (group_name,group_size,comp_date,medal_type) 
    print(group,group_num) 
    group_num += 1


