#!/usr/bin/env python3
"""
Postgresql client example to update a record
"""

import psycopg2

db_host = "localhost"
db_port = 5432
db_user = "myuser"
db_pass = "mypassword"
db_name = "testdb"

# connect to database
db_conn = psycopg2.connect(
    host=db_host, port=db_port, user=db_user, password=db_pass, dbname=db_name
)

# create a cursor object in order to
# interact with the database connection
db_cur = db_conn.cursor()

# setup insert statement
sql_cmd = """UPDATE COMPANY SET address = 'McDonalds'
             WHERE name = 'Ronald'"""

# execute the sql command and commit changes to the db
db_cur.execute(sql_cmd)
db_conn.commit()

# close db connection
db_conn.close()
