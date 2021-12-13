import mysql.connector
#/////////////////////////////////////////////////connect to DB/////////////////////////////////////////////////////////
mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="12345",
    database="library"

)
#//////////////////////////////////////////adding new member////////////////////////////////////////////////////////////
def insertmember():

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


# ///////////////////////////////////////////show a list of books///////////////////////////////////////////////////////
def showbook():


    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM book")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


# //////////////////////////////////////////////////adding new book/////////////////////////////////////////////////////
def insertbook():

    mycursor = mydb.cursor()
    shabak = input("shabak")
    price = input("price")
    sub = input("subject")
    bname = input("bookname")
    count = input("howmany books do you want to add")

    mycursor.execute("SELECT book_name FROM book")
    myresult = mycursor.fetchall()

    if bname in myresult:
        updatecount(shabak, 1)

    sql = "INSERT INTO book (book_name,shabak,price,sub) VALUES (%s, %s ,%s, %s)"

    val = (bname, shabak, price, sub)
    mycursor.execute(sql, val)

    sql = "INSERT INTO counts (book,nums) VALUES (%s, %s)"
    val = (bname,count)
    mycursor.execute(sql, val)
    mydb.commit()


    return ("book", bname,"added")
#///////////////////////////////////////////show the books that you borrowed////////////////////////////////////////////
def checkborrow():

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


# ///////////////////////////////////////////////////borrow a book//////////////////////////////////////////////////////
def borrow():

    shabak=input("plz enter your book shabak")
    ncode=input("plz enter your nathonalcode")

    mycursor = mydb.cursor()


    sql = "SELECT bID FROM book WHERE shabak = " + shabak
    mycursor.execute(sql, )
    myresult1 = mycursor.fetchall()
    print(myresult1)

    sql= "SELECT mID FROM members WHERE ncode = " + ncode
    mycursor.execute(sql, )
    myresult2= mycursor.fetchall()
    print(myresult2)

    sql = "SELECT situ FROM borrow WHERE bID = " + str(myresult1[0][0])
    mycursor.execute(sql, )
    myresult3 = mycursor.fetchall()
    print(myresult3)

    if myresult3[0][0]==1:
        sql = "INSERT INTO borrow (bID, mID) VALUES (%s, %s)"
        val = (str(myresult1[0][0]), str(myresult2[0][0]))
        mycursor.execute(sql, val)
        mydb.commit()
        updatecount(shabak,0)

    else:
        print("sorry,this book is not exist in library now")
#///////////////////////////////////////////////////return book/////////////////////////////////////////////////////////
def returnbook():
    shabak = input("plz enter your book shabak")
    ncode = input("plz enter your nathonalcode")

    mycursor = mydb.cursor()

    sql = "SELECT bID FROM book WHERE shabak = " + shabak
    mycursor.execute(sql, )
    myresult1 = mycursor.fetchall()
    print(myresult1)
    sql = "SELECT situ FROM borrow WHERE bID =" + str(myresult1[0][0])
    mycursor.execute(sql,)
    myresult2 = mycursor.fetchall()
    print(myresult2)
    if myresult2[0][0]==0:

        sql = "UPDATE borrow SET situ = %s WHERE bID = %s"
        val = ("1", myresult1[0][0])

        mycursor.execute(sql, val)

        mydb.commit()


#///////////////////////////////////////////////////update count////////////////////////////////////////////////////////

def updatecount(shabak,check):

        mycursor = mydb.cursor()

        sql = "SELECT book_name FROM book WHERE shabak = " + shabak
        mycursor.execute(sql, )
        x1 = mycursor.fetchall()
        print(x1)


        sql = "SELECT nums FROM counts WHERE book = " + str(x1[0][0])
        mycursor.execute(sql, )
        x=mycursor.fetchall()
        print(x)


        #///////////////////update count for borrow//////////////////////////
        if check==0:
            sql = "UPDATE counts SET nums =" + str(int(x[0][0] - 1)) + "WHERE book=" + str(x1[0][0])

            mycursor.execute(sql, val)
            mydb.commit()
        #//////////////////update count for add book/////////////////////////
        if check==1:
            sql = "UPDATE counts SET nums =" + str(int(x[0][0] + 1)) + "WHERE book=" + str(x1[0][0])
            mycursor.execute(sql,)
            mydb.commit()


#////////////////////////////////////////////////////menue//////////////////////////////////////////////////////////////
x=1
while x!=0:
    menue = int(input("add book:1 , show all books:2 , register:3,check your borrow:4,borrow:5,return6:"))

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
    if menue == 6:
      returnbook()
