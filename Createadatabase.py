#Author: SAHIL SAINI

import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print ("Table created successfully")

conn.close()

##When the above program is executed, it will create
#  the COMPANY table in your test.db and it will 
# display the following messages −

## Opened database successfully
## Table created successfully