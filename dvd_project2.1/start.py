import mysql.connector

'''
ONE TIME CONFIGURATION FILE TO CREATE TABLE AND
ADD DATA VALUES TO TABLE
'''
#MAKE CONNECTION TO DATABASE
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = 'dvd_system_py')

x = mydb.cursor()

'''CREATE TABLE
#x.execute("CREATE TABLE records (
                                     'name' varchar(50) not null, 
                                     'star' varchar(50), 
                                     'costar' varchar(50), 
                                     'yr' int, 
                                     'genre' int not null
                                     )
                                     ")
        '''
sql = "INSERT INTO records (name, star, costar, yr, genre) VALUES (%s,%s,%s,int,int)"
val = ("amy", "me", "you", 1998, 4)
x.execute(sql,val)
x.commit()
x.close()
