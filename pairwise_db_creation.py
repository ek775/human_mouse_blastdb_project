"""
Establishes SQLite database by establishing two tables for each directional alignment.

Run this script from the command line to set up a simple database using the format below:

python pairwise_db_creation.py [extracted_alignments_1].csv [extracted_alignments_2].csv
"""
#import packages
import sys, os
import numpy as np
import sqlite3

#CLI + input checks
file_1 = sys.argv[1]
assert type(file_1)==str
assert file_1[-4:]==".csv"

file_2 = sys.argv[2]
assert type(file_2)==str
assert file_2[-4:]==".csv"

### MAIN ###

#check/clear namespace
os.system('rm pairwise_blast.db') 

### establish database
try: 
    # Making a connection to sqlite3 database
    sqliteConnection = sqlite3.connect('pairwise_blast.db') 
    print("Connected to SQLite") 
except sqlite3.Error as error: 
    print("Failed to connect with sqlite3 database", error) 
finally: 
    # Inside Finally Block, If connection is open, we need to close it 
    if sqliteConnection: 
        sqliteConnection.close() 
        print("the sqlite connection is closed")

### create tables
print('Creating Tables...')
PairwiseConnection = sqlite3.connect('pairwise_blast.db')
Cursor = PairwiseConnection.cursor()

Cursor.execute(f"CREATE TABLE {file_1[:-4]}(accession, hit_id, hit_def, hit_num, hit_len, expect, score, query, subject, match)")
Cursor.execute(f"CREATE TABLE {file_2[:-4]}(accession, hit_id, hit_def, hit_num, hit_len, expect, score, query, subject, match)")

verify = Cursor.execute("SELECT name FROM sqlite_master")
print(verify.fetchall())
print("----- Done -----")

### insert file 1
print(f"Reading in {file_1}...")
df = np.loadtxt(file_1, delimiter=",", dtype=str)

print('Populating Table...')
Cursor.executemany(f"""INSERT INTO {file_1[:-4]} VALUES(?)""", df)
PairwiseConnection.commit()
print("----- First Blast Table Created -----")

# validate
print(Cursor.execute(f"SELECT accession FROM {file_1[:-4]} LIMIT 5").fetchall())

### insert file 2
print(f"Reading in {file_2}...")
df = np.loadtxt(file_2, delimiter=",", dtype=str)

print('Populating Table...')
Cursor.executemany(f"""INSERT INTO {file_2[:-4]} VALUES(?)""", df)
PairwiseConnection.commit()
print("----- First Blast Table Created -----")

# validate
print(Cursor.execute(f"SELECT accession FROM {file_2[:-4]} LIMIT 5").fetchall())

### close connection
print("----- Closing Connection -----")
PairwiseConnection.close()

### END ###