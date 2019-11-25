import mysql.connector

def formatting(Title, Star , Costar , Year, Genre):
    return "INSERT INTO records(name, star, costar, yr, genre) values ('{0}', '{1}', '{2}', {3}, {4})".format(Title, Star, Costar, Year, Genre)

def SQLAddDVD(Title, Star, Costar, Year, Genre):
    try:
        mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "dvd_system_py")
        x = mydb.cursor()
        x.execute(formatting(Title, Star = 'null', Costar = 'null', Year= '0', Genre= '0'))
        mydb.commit()
        x.close()
        mydb.close()
        print("record added")
        input("Press Enter to continue: ")
    except:
        print("THERE WAS A PROBLEM ADDING THE RECORD")
        input("Press Enter to continue: ")

def AddDVD():
    print("===============================")
    print("ADD A DVD TO THE DATABASE:")
    print("===============================")
    Title = input("Enter the DVD title: ")
    Star = input("Enter the name of the movie's star: ")
    Costar = input("Enter the name of the movie's costar: ")
    Year = input("Enter the year the movie was released: ")
    Genre =  input("Enter the genre:\n - 0 for unknown, 1 for Drama, 2 for horror, 3 for comedy, 4 for romance: ")
    if Genre == "0" or "1" or "2" or "3" or "4":
        #Genre = "Drama"
        Genre = int(Genre)
    else:
        print("ERROR GETTING INFORMATION!")
        input("Press Enter to return to the menu: ")
        return
    #print(Title, Star, Costar, Year, Genre)
    SQLAddDVD(Title, Star, Costar, Year, Genre)
