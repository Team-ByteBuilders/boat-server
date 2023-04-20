import mysql.connector
import face_recognition
import cv2
import numpy as np
import pickle


def addMonument(name, details, fees, image_url, lat, lon):
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        f"insert into monuments ( name, details, fees, image_url, lat, lon) values('{name}', '{details}', {fees}, '{image_url}', {lat}, {lon})")
    mydb.commit()
    mycursor.close()
    mydb.close()


def getUser(phone):
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor(buffered=True)
    try:
        mycursor.execute(f"select * from users where phone = {phone}")
    except:
        return None
    
    user = None
    for x in mycursor:
        user = x
        break
    if user == None:
        return user
    UserDetails = {
        "name": user[0],
        "money": user[1],
        "age": user[2],
        "id": user[4],
        "phone": user[5]
    }
    mydb.commit()
    mycursor.close()
    mydb.close()
    return UserDetails


def addUser(name, age, face, phone):
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor()
    enconding = face_recognition.face_encodings(face)[0]
    mycursor.execute(
        f"insert into users ( name, money, age, faceData, phone) values('{name}', 0, {age}, '{enconding}', {phone})")
    mydb.commit()
    mycursor.close()
    mydb.close()
