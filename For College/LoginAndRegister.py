from DatabaseCode import *

SecurityQuestions = {
    1: "What is your nickname: ",
    2: "What is the name of your school: ",
    3: "Where were you born: ",
}


def checkQuestions(question, no, user):
    while True:
        ans = input(question)
        print()
        check = checkSecurityQuestion(no, ans, user)
        if check == "incorrect":
            print("Incorrect Answer\nPlease answer again\n")
        else:
            return True


def login():
    user = input("Enter username: ")
    if not checkUser(user.lower()):
        print("No such User exists")
        print("Please register first")
        return "register"
    while True:
        password = input("Enter password: ")
        check = loginUser(user, password)
        if check == "incorrect":
            while True:
                ch = input("\nDo you wanna change password? (Yes/No): ").lower()
                if ch == "yes":
                    if checkQuestions(SecurityQuestions[1], 1, user):
                        if checkQuestions(SecurityQuestions[2], 2, user):
                            if checkQuestions(SecurityQuestions[3], 3, user):
                                password = input("Enter new password: ")
                                changeUserPassword(password, user)
                elif ch == "no":
                    break
                else:
                    print("Wrong choice")
        else:
            break
    return user


def register():
    while True:
        username = input("Enter username: ")
        if checkUser(username.lower()):
            print("User already exists\n")
            print("Please Login instead")
            print()
            return "login"
        else:
            password = input("Enter password: ")
            print("\nSecurity question\n")
            ans1 = input(SecurityQuestions[1]).lower()
            ans2 = input(SecurityQuestions[2]).lower()
            ans3 = input(SecurityQuestions[3]).lower()
            registerUser(username, password, ans1, ans2, ans3)
            return username
