import mysql.connector, csv

#FUNCTION TO WRITE ENTIRE DVD LIST TO CSV
def WriteCSV():

    SQL = "SELECT * FROM records"

    try:
        mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "dvd_system_py")
        x = mydb.cursor()
        x.execute(SQL)
        output = x.fetchall()
        x.close()
        mydb.close()

    except:
        print("THERE WAS A PROBLEM ACCESSING THE DATABASE!")
        input("Press Enter to return to the menu: ")
        return
    try:
        print("===============================")
        print("EXPORT DATABASE TO CSV:")
        print("===============================")
        filename = input("Enter base filename (will be given a .csv extension): ")
        filename = filename + ".csv"
        writer = csv.writer(open(filename, "w+"))
        writer.writerow(("TITLE", "STAR NAME", "COSTAR NAME", "YEAR", "GENRE"))
        writer.writerows(output)
        print(filename, " successfully written, press Enter to continue:  ")
        input("")
        return
    except:
        print("ERROR WRITING FILE!")
        input("Press Enter to return to the menu: ")

