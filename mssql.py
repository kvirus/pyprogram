import pyodbc

#Параметры подключения
driver = 'DRIVER={SQL Server}'
server = 'virtus_pc'
#port = 'PORT=1433'
db = 'tempdb'
user = 'sa'
pw = 'Z'

conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+db+'; UID='+user+'; PWD='+pw+'')
cursor = conn.cursor()
cursor.execute('create table NewTable (id int)')

conn.commit()
conn.close()