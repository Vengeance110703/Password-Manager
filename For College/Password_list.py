from Password_generator import *
from DatabaseCode import *


def passwordList(user):
    while True:
        row = checkPasswordList(user)
        if row == 0:
            print("There are no Usernames or Passwords associated with your account")
            while True:
                ch = input(
                    "Do you want to add a username & password (Yes/No): "
                ).lower()
                if ch == "yes":
                    username = input("\nEnter username: ")
                    password = input("Enter password: ")
                    addPassword(user, username, password)
                    print("\nUsername and Password saved successfully")
                    break
                elif ch == "no":
                    return
                else:
                    print("Wrong choice\n")
        else:
            showPasswordList(user)
            while True:
                print()
                print("1. Add Username & Password")
                print("2. Update Username")
                print("3. Update Password")
                print("4. Delete Username & Password")
                print("5. Exit\n")
                ch = int(input("Enter choice: "))
                if ch == 1:
                    username = input("\nEnter username: ")
                    password = input("Enter password: ")
                    addPassword(user, username, password)
                    print("\nUsername and Password saved successfully\n")
                    showPasswordList(user)
                elif ch == 2:
                    index = int(input("Enter Sr. No. of the username: "))
                    username = input("Enter new username: ")
                    updateEntry(user, "username", username, index)
                    print("\nUsername updated successfully\n")
                    showPasswordList(user)
                elif ch == 3:
                    index = int(input("Enter Sr. No.: "))
                    username = input("Enter new password: ")
                    updateEntry(user, "password", username, index)
                    print("\nUsername updated successfully\n")
                    showPasswordList(user)
                elif ch == 4:
                    index = int(input("Enter Sr. No. to delete: "))
                    print("\nUsername and Password deleted successfully\n")
                    deleteEntry(user, index)
                    break
                elif ch == 5:
                    break
                else:
                    print("Wrong Choice")
            if ch == 5:
                break


def passwordGenerator():
    while True:
        print("Do you want to customize the options or go with the Default settings?\n")
        print(
            "1. Default [Numbers: Yes, Lowercase: Yes, Uppercase: Yes, Special characters: Yes, Length: 12]"
        )
        print("2. Customize\n")
        ch = int(input("Enter choice: "))
        print()
        if ch == 1:
            return generator(12, [True, True, True, True])
        elif ch == 2:
            print("What do you want in your password? (Yes/No): ")
            choice = []
            choice.append(input("Digits: ").lower())
            choice.append(input("lowercase letters: ").lower())
            choice.append(input("Uppercase letters: ").lower())
            choice.append(input("Special characters: ").lower())
            choicetorf = list(map((lambda x: True if x == "yes" else False), choice))
            max_len = int(input("What will be the length of the password: "))
            print()
            return generator(max_len, choicetorf)
        else:
            print("Wrong choice\n")


def passwords(user):
    while True:
        print()
        print("1. Show Password list")
        print("2. Random Password Generator")
        print("3. Logout\n")
        ch = int(input("Enter choice: "))
        print()
        if ch == 1:
            passwordList(user)
        elif ch == 2:
            random_password = passwordGenerator()
            print(random_password)
            while True:
                ch = input("\nDo you wanna save password (Yes/No): ").lower()
                if ch == "yes":
                    username = input("Enter username associated with password: ")
                    addPassword(user, username, random_password)
                    print("Username and Password saved successfully")
                    break
                if ch == "no":
                    break
                else:
                    print("Wrong choice\n")
        elif ch == 3:
            break
        else:
            print("Wrong choice\n")
