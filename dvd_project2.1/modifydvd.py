import mysql.connector

def ModifyDVD():

    print("===============================")
    print("MODIFY A DVD RECORD:")
    print("===============================")

    dvdTitle = input("\nEnter the title of the DVD to modify: ")

    SQL_LOOKUP = "SELECT * FROM records WHERE name = '{}'".format(dvdTitle)

    try:
        mydb = mysql.connector.connect(host = "localhost", user = 'root', passwd = 'root', database = 'dvd_system_py')
        x = mydb.cursor()
        x.execute(SQL_LOOKUP)
        searchResult = x.fetchall()
        if searchResult==0:
            print("No record found")
    except:
        print("THERE WAS A PROBLEM ACCESSING THE RECORD IN THE DATABASE!")
        input("Press Enter to continue: ")
        return

    try:
        print("===============================")
        print("DVD TO MODIFY:")
        print("===============================")
        print("1 - Title:\t", searchResult[0][0])
        print("2 - Star:\t", searchResult[0][1])
        print("3 - Costar:\t", searchResult[0][2])
        print("4 - Year:\t", searchResult[0][3])
        print("5 - Genre:\t", searchResult[0][4])
        print("===============================")

        choice = input("Type the number for the field \
        \nyou want to modify and press Enter: ")

        titleChanged = False
        modify = ""
        newvalue = ""
        if choice == "1":
                modify = "name"
                newvalueTitle = input("Enter the new DVD title name: ")
                newvalue = "'{}'".format(newvalueTitle)
                titleChanged = True
        elif choice == "2":
            modify = "star"
            newvalue = input("Enter the new DVD star name: ")
            newvalue = "'{}'".format(newvalue)
        elif choice == "3":
            modify = "costar"
            newvalue = input("Enter the new DVD costar name: ")
            newvalue = "'{}'".format(newvalue)
        elif choice == "4":
            modify = "yr"
            newvalue = input("Enter the new DVD year of release: ")
            newvalue = "'{}'".format(newvalue)
        elif choice == "5":
            modify = "genre"
            print("===============================")
            print("Enter the genre to apply to this DVD:")
            print("1 - Drama")
            print("2 - Horror")
            print("3 - Comedy")
            print("4 - Romance")

            newvalue = input("Type the number for the genre \
                        \nyou want to apply and press Enter: ")

        SQL_UPDATE = "UPDATE records SET {} = {} WHERE name = '{}'".format(modify, newvalue, dvdTitle)

        mydb = mysql.connector.connect(host="localhost", user='root', passwd='root', database='dvd_system_py')
        x = mydb.cursor()
        x.execute(SQL_UPDATE)
        mydb.commit()

        if titleChanged:
            SQL_LOOKUP = "SELECT * FROM records WHERE name = '{}'".format(newvalueTitle)

        #x = mydb.cursor()
        x.execute(SQL_LOOKUP)
        modifyResult = x.fetchall()
        x.close()
        mydb.close()
    except:
        print("THERE WAS A PROBLEM MODIFYING THE RECORD")
        input("Press Enter to continue: ")
        return

    print("MODIFIED RECORD:")
    print("===============================")
    print("===============================")
    print("1 - Title:\t", modifyResult[0][0])
    print("2 - Star:\t", modifyResult[0][1])
    print("3 - Costar:\t", modifyResult[0][2])
    print("4 - Year:\t", modifyResult[0][3])
    print("5 - Genre\t", modifyResult[0][4])
    print("===============================")
    input("Press enter to continue: ")
