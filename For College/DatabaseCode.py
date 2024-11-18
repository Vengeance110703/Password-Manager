import mysql.connector
import os
from dotenv import load_dotenv
import argon2
from tabulate import tabulate

load_dotenv()

ph = argon2.PasswordHasher()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
)


def checkUser(username):
    mycursor = mydb.cursor()

    sql = f"SHOW DATABASES LIKE '{username}'"
    mycursor.execute(sql)

    db = []
    for x in mycursor:
        db.append(x[0])

    return True if len(db) > 0 else False


def registerUser(username, password, ans1, ans2, ans3):
    query = f"CREATE DATABASE {username};"
    mydb.cursor().execute(query)

    query = f"""CREATE TABLE {username}.credentials 
    (id INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(255), 
    password VARCHAR(255),
    ans1 VARCHAR(255),
    ans2 VARCHAR(255),
    ans3 VARCHAR(255));"""
    mydb.cursor().execute(query)

    query = f"""CREATE TABLE {username}.passwords 
    (id INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(255), 
    password VARCHAR(255));"""
    mydb.cursor().execute(query)

    hashpass = ph.hash(password)
    hashans1 = ph.hash(ans1)
    hashans2 = ph.hash(ans2)
    hashans3 = ph.hash(ans3)

    query = f"""INSERT INTO {username}.credentials (username, password, ans1, ans2, ans3) 
    VALUES (%s, %s, %s, %s, %s)"""
    values = (username, hashpass, hashans1, hashans2, hashans3)
    mydb.cursor().execute(query, values)

    mydb.commit()


def loginUser(username, password):
    mycursor = mydb.cursor()
    query = f"SELECT password FROM {username}.credentials"
    mycursor.execute(query)

    hash = ""
    for x in mycursor:
        hash = str(x[0])

    try:
        if ph.verify(hash, password):
            print("Correct Password")
    except:
        print("Incorrect Password")
        return "incorrect"


def checkSecurityQuestion(no, ans, user):
    mycursor = mydb.cursor()
    sql = f"SELECT ans{no} FROM {user}.credentials"
    mycursor.execute(sql)

    hash = ""
    for x in mycursor:
        hash = str(x[0])

    try:
        if ph.verify(hash, ans):
            print("Correct Answer")
    except:
        return "incorrect"


def changeUserPassword(password, user):
    hashpass = ph.hash(password)
    sql = f"UPDATE {user}.credentials SET password = '{hashpass}' WHERE id = 1"
    mydb.cursor().execute(sql)
    mydb.commit()


def checkPasswordList(user):
    sql = f"SELECT COUNT(*) AS row_count FROM {user}.passwords"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    for x in mycursor:
        return x[0]


def showPasswordList(user):
    mycursor = mydb.cursor()
    sql = f"SELECT username,password FROM {user}.passwords"
    mycursor.execute(sql)
    data = []
    cnt = 1
    for x in mycursor:
        x = list(x)
        x.insert(0, cnt)
        data.append(x)
        cnt = cnt + 1
    headers = ["Sr. No.", "Username", "Password"]
    print(tabulate(data, headers))


def addPassword(user, username, password):
    sql = f"INSERT INTO {user}.passwords (username, password) VALUES ('{username}', '{password}')"
    mydb.cursor().execute(sql)
    mydb.commit()


def deleteEntry(user, id):
    sql = f"DELETE FROM {user}.passwords WHERE id IN ( SELECT id FROM ( SELECT id FROM {user}.passwords ORDER BY id LIMIT 1 OFFSET {id - 1} ) AS subquery )"
    mydb.cursor().execute(sql)
    mydb.commit()


def updateEntry(user, column, entry, id):
    sql = f"UPDATE {user}.passwords SET {column} = '{entry}' WHERE id IN ( SELECT id FROM ( SELECT id FROM {user}.passwords ORDER BY id LIMIT 1 OFFSET {id - 1} ) AS subquery )"
    mydb.cursor().execute(sql)
    mydb.commit()
