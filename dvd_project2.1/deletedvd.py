import mysql.connector

#RUN THE SQL STATEMENT TO DELETE THE SELECTED RECORD
def SQLDeleteDVD(dvdToDelete):
    try:
        SQL_DELETE = "DELETE FROM records WHERE name = '{}'".format(dvdToDelete)

        mydb = mysql.connector.connect(host="localhost", user='root', passwd='root', database='dvd_system_py')
        x = mydb.cursor()
        x.execute(SQL_DELETE)
        mydb.commit()
        x.close()
        mydb.close()
        input("Item deleted, press enter to continue: ")
    except:
        print( "THERE WAS A PROBLEM DELETING THE RECORD")
        input("Press Enter to continue: ")


#TAKE USER INPUT AND RUN FUNCTION TO DELETE THE SELECTED RECORD
def DeleteDVD():

    #os.system('cls')
    print("===============================")
    print("DELETE A DVD RECORD:")
    print("===============================")

    dvdToDelete = input("\nEnter the title of the DVD to delete:\t")
    SQL_LOOKUP = "SELECT * FROM records WHERE name = '{}'".format(dvdToDelete)
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="dvd_system_py")
        x = mydb.cursor()
        x.execute(SQL_LOOKUP)
        searchResult = x.fetchall()
        if searchResult[0] == ():
            print("No record found")
            x.close()
            mydb.close()
            return
    except:
        print("THERE WAS A PROBLEM ACCESSING THE RECORD IN THE DATABASE!")
        input("Press Enter to continue: ")
        return

    print("===============================")
    print("DVD TO DELETE:")
    print("===============================")
    print("Title:\t", searchResult[0][0])
    print("Star:\t", searchResult[0][1])
    print("Costar:\t", searchResult[0][2])
    print("Year released:\t", searchResult[0][3])
    print("Genre:\t:", searchResult[0][4])
    print("===============================")
    print('''
    Are you sure you want to delete?  Enter a choice and press enter
    (Y/y = yes, Anything else = No)
    ''')
    choice = input("\t")

    if choice == "Y" or choice == "y":
        SQLDeleteDVD(dvdToDelete)
    else:
        x.close()
        mydb.close()
        input("Item NOT deleted, press enter to continue: ")