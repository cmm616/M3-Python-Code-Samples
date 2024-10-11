#Corinthian M
#Oct 8, 2024 
#Code ask the user for their name.
name = input("What is your name? ")
#Code to greet the user with the imputed name.
print("Hello, {name}!")
#2a. Code for authorized users.
authorized_users = ["Corinthain", "Ben"]
#2a. Code to check if the user is authorized, if user imputs a name not in the authorized list the code give them an "Unauthorized User" text output.
if name in authorized_users:
    print("Hello, {name}!")
else:
    print("Unauthorized user.")