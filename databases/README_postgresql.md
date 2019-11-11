# Postgres Database Setup

## Install Packages

Install postgres db, client

```bash
sudo apt install postgresql postgresql-client
```

## Python Setup

Install library required for Python's pyscopg2

```bash
sudo apt install libpq-dev
```

Install Python3 psycogp2

```bash
pip3 install psycopg2 --user
```

## Configure Database

Switch to postgres user and open postgres prompt

```bash
sudo su - postgres
psql
```

### Create a new database

List databases

```bash
postgres=# \l
```

Create database

```sql
postgres=#
create database testdb;
```

Connect/use the new database

```bash
postgres=# \c testdb
```

### Create a new table

Describe all tables in the database

```bash
postgres=# \d
```

Create table

```sql
testdb=#
CREATE TABLE COMPANY(
    ID       SERIAL PRIMARY KEY,
    NAME     TEXT    NOT NULL,
    AGE      INT     NOT NULL,
    ADDRESS  CHAR(50),
    SALARY   REAL
 );
```

Describe specific table

```bash
postgres=# \d company
```

Display all rows in the company table

```sql
testdb=#
select * from company;
```

### Insert data into the table

Insert some new data

```sql
testdb=#
INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ('Paul', 32, 'California', 20000.00);

insert into company (name,age,address,salary) values ('Robert', 10, 'Moms Basement', 40000.00);
```

### DB User Setup

Create a user, grant full access to the new test database and tables

```sql
create user myuser with password 'mypassword';
grant all on DATABASE testdb TO myuser;
grant ALL on TABLE company TO myuser;
# id_seq table auto created due to "serial" data type of the primary key
grant ALL on TABLE company_id_seq TO myuser;
```

To connect as that user:

```bash
testdb=# \q
sudo su - postgres
psql -h localhost -U myuser testdb
```
