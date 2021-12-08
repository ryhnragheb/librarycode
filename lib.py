import mysql.connector


# register
def insertmember():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO members (name, lname, ncode,phone) VALUES (%s, %s ,%s, %s)"
    name = input("name")
    lname = input("lastname")
    ncode = input("ncode")
    phone = input("phone")
    val = (name, lname, ncode, phone)
    mycursor.execute(sql, val)
    mydb.commit()
    return ("member", name, lname , "added")


# /////////////////////////////////////////////////////////////////////////////////////
def showbook():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )


    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM books")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


# ///////////////////////////////////////////////////////////////////////////////////
def insertbook():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO books (book_name,shabak,price,sub) VALUES (%s, %s ,%s, %s)"
    shabak = input("shabak")
    price = input("price")
    sub = input("subject")
    bname = input("bookname")

    val = (bname, shabak, price, sub)
    mycursor.execute(sql, val)

    mydb.commit()
    return ("book", bname,"added")


# ///////////////////////////////////////////////////////////////////////////
x=1
while x!=0:
    menue = int(input("add book:1 , show all books:2 , register:3, exit:0"))

    if menue == 1:
        print(insertbook())
    if menue == 2:
        showbook()
    if menue == 3:
        print(insertmember())
