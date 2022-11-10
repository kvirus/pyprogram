import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=Z',autocommit=True)
    cursor = conn.cursor()
    #cursor.execute('CREATE DATABASE test')
    cursor.execute('USE test')
    # cursor.execute('INSERT INTO phones VALUES (1,2,562)')
    # cursor.execute('INSERT INTO phones VALUES (34,55,8123)')
    #cursor.execute('CREATE TABLE phones2 (id int IDENTITY, Name varchar(20), last varchar (20), phone BIGINT)')
    #cursor.execute("INSERT INTO phones2 VALUES ('Fedya','Rushpil',23448123)")
    cursor.execute("SELECT * FROM phones2 WHERE  (Name = 'fedya')")
    print(cursor)
    # cursor.execute('CREATE DATABASE testDB3')
    # cursor.execute('USE testDB3')
    # cursor.execute('CREATE TABLE newTable (id int,name int)')
    conn.commit()
    conn.close()
    for i in coursor:
        print(i)
except Exception as bad:
    print(bad)



