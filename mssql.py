import pyodbc

#Параметры подключения
#driver = 'DRIVER={SQL Server}'
server = 'virtus_pc'
#port = 'PORT=1433'
db = 'tempdb'
user = 'sa'
pw = 'Z'
#x=input('введите название базы',)
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+db+'; UID='+user+'; PWD='+pw+'')
cursor = conn.cursor()
#cursor.execute('CREATE DATABASE newbase')

#conn.commit()
conn.close()