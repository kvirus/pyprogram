import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=test;UID=sa;PWD=Z',autocommit=True)
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE testDB3')
    cursor.execute('USE testDB3')
    cursor.execute('CREATE TABLE newTable (id int,name int)')
    conn.commit()
    conn.close()
    for i in coursor:
        print(i)
except Exception as bad:
    print(bad)



