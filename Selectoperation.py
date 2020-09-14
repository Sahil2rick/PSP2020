#Author: SAHIL SAINI


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print ("Operation done successfully")
conn.close()


#When the above program is executed, it will produce the following result.

#Opened database successfully
#ID = 1
#NAME = Paul
#ADDRESS = California
#SALARY = 20000.0

#ID = 2
#NAME = Allen
#ADDRESS = Texas
#SALARY = 15000.0

#ID = 3
#NAME = Teddy
#ADDRESS = Norway
#SALARY = 20000.0

#ID = 4
#NAME = Mark
#ADDRESS = Rich-Mond
#SALARY = 65000.0

#Operation done successfully