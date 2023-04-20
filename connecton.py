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

def checkUser(phone):
    mydb = mysql.connector.connect(
        host="containers-us-west-137.railway.app",
        user="root",
        password="KK1JadM51ULeSNrI0NG2",
        database="railway",
        port=6503
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(f"select * from users where phone = {phone}")
    print("Executed")
    found = False
    for x in mycursor:
        found = True
        print(x)
    
    mydb.commit()
    mycursor.close()
    mydb.close()

    return found