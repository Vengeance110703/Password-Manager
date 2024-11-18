from LoginAndRegister import *
from Password_list import *


while True:
    print("1. Login")
    print("2. Register")
    print("3. Random Password Generator\n")
    ch = int(input("Enter choice: "))
    print()

    if ch == 1:
        user = login()
        if not user == "register":
            passwords(user)
    elif ch == 2:
        user = register()
        if not user == "login":
            passwords(user)
    elif ch == 3:
        print(
            "The Generator gives passwords with Numbers, Lowercase & Uppercase letters & Special Character"
        )
        while True:
            print("Random Password: " + passwordGenerator())
            print()
            ch = input("Do you want another random password (Yes/No): ").lower()
            if ch == "yes":
                continue
            elif ch == "no":
                break
            else:
                print("Wrong option")
        print()
    else:
        print("Wrong option")
        print()
