#!/usr/bin/env python3
"""
MySQL client example to select/display records
"""

import pymysql

db_host = "localhost"
db_port = 3306
db_user = "myuser"
db_pass = "mypassword"
db_name = "testdb"

# connect to database
db_conn = pymysql.connect(
    host=db_host, port=db_port, user=db_user, password=db_pass, dbname=db_name
)

# create a cursor object in order to
# interact with the database connection
db_cur = db_conn.cursor()

# query the table
db_cur.execute("SELECT name,salary FROM company")

# print results
for name, salary in db_cur.fetchall():
    print(f"> {name} (${salary})")

# close db connection
db_conn.close()
