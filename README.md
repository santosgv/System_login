# System_login

### Simple Login System using Tkinter and Sqlserver

#### To validate the login, it is necessary to have data in the table where it is consulted.

with function for create acount


## For it to work properly, it is necessary to have a database server installed on the machine locally. db [MasterDB] used in the db.py script and have a table created [Login] as in the example.

![Imagen_DB](https://github.com/santosgv/System_login/blob/master/db.png)




both the database and the table can be changed to the name you want, just adjust in the [db.py] file


### Script create table "login"

create database [login]
(

    [userID] primary key idantity not null,
    [Login] varchar(20),
    [Password]varchar(20),
    [situacion]bit defalt 0
    
 );
);
