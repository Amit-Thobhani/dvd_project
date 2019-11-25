import add_DVD
import lookupdvd
import modifydvd
import deletedvd
import writecsv
def menu():
    print("""
    ================================
    DVD DATABASE
    ================================
    1 - Add a DVD to the database
    2 - Search inventory
    3 - Modify DVD record
    4 - Delete DVD record
    5 - Export listing to CSV
    6 - Exit
    ================================
    """)
    choice = input("Enter a choice and press enter: ")
    return choice

# starting user input

choice = ""

while choice != '6':
    choice = menu()
    if choice == '1':
        #os.system('cls')
        #print("add dvd")
        add_DVD.AddDVD()
    elif choice == '2':
        #os.system('cls')
        #print("=>search inventory")
        lookupdvd.lookupDVD()
    elif choice == '3':
        #os.system('cls')
        #print("Modify record")
        modifydvd.ModifyDVD()
    elif choice == '4':
        #os.system("cls")
        #print("delete record")
        deletedvd.DeleteDVD()
    elif choice == '5':
        #os.system('cls')
        #print("export in csv")
        writecsv.WriteCSV()

print("Thank you")