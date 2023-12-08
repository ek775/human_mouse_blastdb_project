"""
Execute this script from the command line to query the database.

Using this since turbogears is having installation / dependency issues
"""

import sys
import sqlite3

#user should pass in a db here
database = sys.argv[1]

print("Establishing Connection...")
try:
    connection = sqlite3.connect(database)
    Cursor = sqlite3.Cursor(connection)
    print("---Connected---")
except:
    print("Unable to connect")
    exit(1)

### MAIN ###
q = True
while q==True:
    query = input("Enter Query? [press enter or type 'q' to quit]")
    if query.strip()=='q':
        exit(0)

    #prompted query
    _select_ = input("SELECT:")
    _from_ = input("FROM:")
    _where_ = input("WHERE:")
    _groupby_ = input("GROUPBY:")
    _having_ = input("HAVING:")
    _orderby_ = input("ORDER BY:")
    _limit_ = input("LIMIT:")
    
    params = [_select_, _from_, _where_, _groupby_, _having_, _orderby_, _limit_]
    param_names = ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY', 'LIMIT']

    #clean params, generate sql
    sql = ""
    for i,j in enumerate(params):
        j=''.join(j.split())
        if j != None:
            sql.join(param_names[i]+' '+j+' ')
        else:
            continue

    #confirm query
    print(sql)
    confirm = input("Execute Query? [y/n]")

    #if confirmed
    if confirm.strip()=='y':
        #attempt query
        try:
            result = Cursor.execute(sql)
            result.fetchall()
        except sqlite3.Error as error:
            print("Bad query:", error)
    #if denied, try query entry again
    elif confirm.strip()=='n':
        pass
    else:
        print('Query not confirmed')