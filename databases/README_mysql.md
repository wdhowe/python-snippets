# MySQL/MariaDB Database Setup

## Install Packages

Install mysql db, client

```bash
sudo apt install mariadb-server mariadb-client
```

## Python Setup

Install Python3 pymysql

```bash
pip3 install pymysql --user
```

## Configure Database

Start/enable the service and run the post install secure configuration utility

```bash
sudo systemctl start mysqld
sudo systemctl enable mysqld
sudo mysql_secure_installation
```

### Create a new database

Connect to the database

```bash
mysql -u root -p
```

List databases

```sql
MariaDB [(none)]> show databases;
```

Create database

```sql
MariaDB [(none)]> CREATE DATABASE testdb;
```

Connect/use the new database

```bash
MariaDB [(none)]> USE testdb;
```

### Create a new table

Describe all tables in the database

```bash
MariaDB [testdb]> SHOW TABLES;
```

Create table

```sql
MariaDB [testdb]>
CREATE TABLE COMPANY(
    ID       SERIAL PRIMARY KEY,
    NAME     TEXT    NOT NULL,
    AGE      INT     NOT NULL,
    ADDRESS  CHAR(50),
    SALARY   REAL
 );
```

Display all rows in the company table

```sql
MariaDB [testdb]>
select * from company;
```

### Insert data into the table

Insert some new data

```sql
MariaDB [testdb]>
INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) VALUES ('Paul', 32, 'California', 20000.00);

insert into company (name,age,address,salary) values ('Robert', 10, 'Moms Basement', 40000.00);
```

### DB User Setup

Create a user, grant full access to the new test database and tables

```sql
MariaDB [(none)]>
CREATE USER myuser@localhost IDENTIFIED by 'mypassword';

grant all on testdb.* TO myuser@localhost;

# flush privileges for changes to take affect now
MariaDB [(none)]>
FLUSH PRIVILEGES;
```

To connect as that user:

```bash
mysql -h localhost -u myuser -p
```
