from getpass import getpass

u = "hehe"
p = "mama mo"

isLogin = False

while isLogin == False:
    username = input("What is your username? --> ")
    password = getpass("What is your password? --> ")

    if u == username and p == password:
        print("LOGIN SUCCESFUL")
        isLogin = True
    else:
        print("LOGIN DENIED")
        isLogin = False