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
    sql = "INSERT INTO book (book_name,shabak,price,sub,count) VALUES (%s, %s ,%s, %s, %s)"
    shabak = input("shabak")
    price = input("price")
    sub = input("subject")
    bname = input("bookname")
    count=input("howmany books do you want to add")

    val = (bname, shabak, price, sub,count)
    mycursor.execute(sql, val)

    mydb.commit()
    return ("book", bname,"added")
#/////////////////////////////////////////////////////////////////////////////
def checkborrow():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )

    mycursor = mydb.cursor()

    nc = input("plz enter your nationalcode:")
    sql = "SELECT mID FROM members WHERE ncode = " + nc
    mycursor.execute(sql,)

    myresult = mycursor.fetchall()


    sql = "SELECT bID FROM borrow WHERE mID ="+str(myresult[0][0])

    mycursor.execute(sql,)

    myresult = mycursor.fetchall()
    print(myresult)

    sql = "SELECT book_name FROM books WHERE bID =" + str(myresult[0][0])

    mycursor.execute(sql,)

    myresult = mycursor.fetchall()
    print(myresult)


# ///////////////////////////////////////////////////////////////////////////
def borrow():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )
    shabak=input("plz enter your book shabak")
    ncode=input("plz enter your nathonalcode")

    mycursor = mydb.cursor()


    sql = "SELECT bID FROM books WHERE shabak = " + shabak
    mycursor.execute(sql, )
    myresult1 = mycursor.fetchall()


    sql= "SELECT mID FROM members WHERE ncode = " + ncode
    mycursor.execute(sql, )
    myresult2= mycursor.fetchall()


    sql = "INSERT INTO borrow (bID, mID) VALUES (%s, %s)"
    val = (str(myresult1[0][0]), str(myresult2[0][0]))
    mycursor.execute(sql, val)
    result=mycursor.fetchall()


#//////////////////////////////////////////////////////////////////////////
x=1
while x!=0:
    menue = int(input("add book:1 , show all books:2 , register:3,check your borrow:4,borrow:5"))

    if menue == 1:
        print(insertbook())
    if menue == 2:
        showbook()
    if menue == 3:
        print(insertmember())
    if menue == 4:
        checkborrow()
    if menue == 5:
        borrow()
