#Author: SAHIL SAINI

import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully")


## Here, you can also supply database name as the special name :memory: 
# to create a database in RAM. Now, let's run the above program to 
# create our database test.db in the current directory. You can 
# change your path as per your requirement. Keep the above code in
#  sqlite.py file and execute it as shown below. If the database is 
# successfully created, then it will display the following message.

## $chmod +x sqlite.py
## $./sqlite.py
## Open database successfully