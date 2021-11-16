import sqlite3
# backend

def studentData():
    # connecting to the sqlite3
    con = sqlite3.connect("student.db")
    cur = con.cursor()

    #creating a table and adding the items in the table
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,StID text, Firstname text, Surname text, DoB text, Age text, Gender text, Address text,Mobile text)")
    con.commit()
    con.close()


# to add and show the database t
def addStdRec( StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    # connecting to the sqlite3
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile) )
    con.commit()
    con.close()

#view function
def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT  * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

# delete function
def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=? " , (id,))
    con.commit()
    con.close()

def searchData(StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    #print("hello5")
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    #print(rows)
    con.close()
    return rows


def dataUpdate(id, StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?,Firstname=?,Surname=?,DoB=?, Age=?,Gender=?,Address=?,Mobile=?, WHERE id=?", (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()




