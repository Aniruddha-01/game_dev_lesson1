user_name = input("Enter your name ")
user_age = int(input("Enter your age "))
user_job = input("Enter your occupation here ")


user_info = {"name":user_name,"age":user_age,"occupation":user_job}
username = user_info["name"]
print(username)

conformation = input("Do you want to change anything?")



print("Enter the new values")
user_name = input("Enter your name ")
user_age = int(input("Enter your age "))
user_job = input("Enter your occupation here ")
user_info["name"] = user_name
user_info["age"] = user_age
user_info["occupation"] = user_job

userage = user_info["age"]
print(userage)
