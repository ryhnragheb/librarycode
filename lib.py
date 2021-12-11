import mysql.connector


#//////////////////////////////////////////adding new member////////////////////////////////////////////////////////////
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


# ///////////////////////////////////////////show a list of books///////////////////////////////////////////////////////
def showbook():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )


    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM book")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


# //////////////////////////////////////////////////adding new book/////////////////////////////////////////////////////
def insertbook():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        password="12345",
        database="library"

    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO book (book_name,shabak,price,sub) VALUES (%s, %s ,%s, %s)"
    shabak = input("shabak")
    price = input("price")
    sub = input("subject")
    bname = input("bookname")
    count =input("howmany books do you want to add")

    val = (bname, shabak, price, sub)
    mycursor.execute(sql, val)

    sql = "INSERT INTO counts (book,nums) VALUES (%s, %s)"
    val = (bname,count)
    mycursor.execute(sql, val)
    mydb.commit()
    
    #updatecount(shabak, 1) 
    
    return ("book", bname,"added")
#///////////////////////////////////////////show the books that you borrowed////////////////////////////////////////////
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


# ///////////////////////////////////////////////////borrow a book//////////////////////////////////////////////////////
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


    sql = "SELECT bID FROM book WHERE shabak = " + shabak
    mycursor.execute(sql, )
    myresult1 = mycursor.fetchall()
    print(myresult1)

    sql= "SELECT mID FROM members WHERE ncode = " + ncode
    mycursor.execute(sql, )
    myresult2= mycursor.fetchall()
    print(myresult2)

    sql = "INSERT INTO borrow (bID, mID) VALUES (%s, %s)"
    val = (str(myresult1[0][0]), str(myresult2[0][0]))
    print(val)
    mycursor.execute(sql, val)
    mydb.commit()
    """updatecount(shabak,0)"""
#///////////////////////////////////////////////////update count////////////////////////////////////////////////////////

def updatecount(shabak,check):
        mydb = mysql.connector.connect(
            host="localhost",
            user="user1",
            password="12345",
            database="library"

        )
        mycursor = mydb.cursor()

        sql = "SELECT book_name FROM book WHERE shabak = " + shabak
        mycursor.execute(sql, )
        x = mycursor.fetchall()
        print(x)


        sql = "SELECT nums FROM counts WHERE book = " + str(x[0][0])
        mycursor.execute(sql, )
        x=mycursor.fetchall()
        print(x)

        """sql = "UPDATE count SET num ="+str(x[0][0])+"WHERE num="+str(int(x[0][0]-1))"""
        #///////////////////update count for borrow//////////////////////////
        if check==0:
            sql = "UPDATE  counts nums = %s WHERE nums = %s"
            val = ("str(int(x[0][0]-1)", "str(x[0][0]")
    
            mycursor.execute(sql, val)
            mydb.commit()
        #//////////////////update count for add book/////////////////////////
        if check==1:
            sql = "UPDATE  counts nums = %s WHERE nums = %s"
            val = ("str(int(x[0][0]+1)", "str(x[0][0]")

            mycursor.execute(sql, val)
            mydb.commit()




#////////////////////////////////////////////////////menue//////////////////////////////////////////////////////////////
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
