import mysql.connector

#RUN THE SQL STATEMENT TO QUERY THE DATABASE
def SQLLookupDVD(searchby, searchtext):
    SQL = "SELECT * FROM records WHERE {0} = '{1}'".format(searchby, searchtext)
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="dvd_system_py")
        x = mydb.cursor()
        x.execute(SQL)
        output = x.fetchall()
        x.close()
        mydb.close()
    except:
        #print(SQL)
        print("THERE WAS A PROBLEM ACCESSING THE DATABASE")
        input("Press Enter to continue: ")
        return

    print("===============================")
    print("DVD SEARCH RESULTS:")
    print("===============================")
    if output == ():
        print("NO RECORDS FOUND")
        print("===============================")
    for entry in output:
        print("Title:\t", entry[0])
        print("Star:\t", entry[1])
        print("Costar:\t", entry[2])
        print("Year:\t", entry[3])
        print("Genre:\t", entry[4])
        print("===============================")
    input("\n\nPress enter to continue: ")

#TAKE USER INPUT AND RUN FUNCTION TO QUERY THE DATABASE
def lookupDVD():
    print ("""
    ===============================
    DVD LOOKUP:
    ===============================
    Enter the criteria to look up by:
    1 - Movie title
    2 - Star
    3 - Costar
    4 - Year released
    5 - Genre""")

    choice = input("\nType a number and press enter: ")

    searchby = ""
    searchtext = ""
    if choice == "1":
        searchby = "name"
        searchtext = input("Enter the DVD title to search for: ")
    elif choice == "2":
        searchby = "star"
        searchtext = input("Enter the DVD star name to search for: ")
    elif choice == "3":
        searchby = "costar"
        searchtext = input("Enter the DVD costar name to search for: ")
    elif choice == "4":
        searchby = "yr"
        searchtext = input("Enter the DVD release year to search for: ")

    elif choice == "5":
        searchby = "genre"
        print("""
        Enter the genre to search for:
        0 - Unknown
        1 - Drama
        2 - Horror
        3 - Comedy
        4 - Romance
        """)
        searchtext = input("\t")

    else:
        print("ERROR IN CHOICE!")
        input("Press Enter to return to the menu: ")
        return

    SQLLookupDVD(searchby, searchtext)
