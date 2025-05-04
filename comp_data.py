
group_num = 1
comp_data = []
for i in range(2):
    print('Group',group_num)
    group_name = input('Enter the name of your group ')
    group_size = input('Enter the size of your group ')
    comp_date = input('Enter the date of the competition in DD-MM-YYYY ')
    medal_type = input('Enter the type of medal recieved ')
    comp_data.append((group_name,group_size,comp_date,medal_type)) 
    group_num += 1


for group in comp_data:
    print("****************************")
    for element in group:
        print(element)