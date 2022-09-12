import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=test;UID=sa;PWD=Zireael')
    coursor = conn.execute('CREATE TABLE dbo.PurchaseOrderDetail
                           (PurchaseOrderID int NOT NULL,LineNumber smallint NOT NUL
                            );')
    for i in coursor:
        print(i)
except Exception as bad:
    print(bad)



