import mysql.connector


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
        print("entered except")
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
        "id": user[3],
        "phone": user[4]
    }
    mydb.commit()
    mycursor.close()
    mydb.close()
    return UserDetails


def addUser(name, age, phone):

    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        f"insert into users ( name, money, age, phone) values('{name}', 0, {age},  {phone})")
    mydb.commit()
    mycursor.close()
    mydb.close()


def getMonuments():
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        f"select * from monuments")
    monumentList = []
    for x in mycursor:
        monument = {
            "name": x[0],
            "details": x[1],
            "fees": x[2],
            "image": x[3],
            "lat": x[4],
            "long": x[5]
        }
        monumentList.append(monument)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return monumentList

def addMoney(money, phone):
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"update users set money = {money} where phone = {phone}")
    mydb.commit()
    mycursor.close()
    mydb.close()
