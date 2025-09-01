
#Create a dictionary 
users = {"alice": "admin",
            "bob": "user"
        }

#Get user input
username = input("Enter username: ")
role = users.get(username, None)
#define login action 
def admin_action():
    print("Admin function executed.")

def user_action():
    print("User function executed.")

#Check role and print message
if role:
    print(f"Welcome {username}! You are a {role}")
    if role == "admin":
        print("Admin access granted.")  
    else:
        print("User acces is granted.")
else:
    print("Access denied.")