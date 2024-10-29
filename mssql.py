import pyodbc

#Параметры подключения
#driver = 'DRIVER={SQL Server}'
server = 'virtus_pc'
#port = 'PORT=1433'
db = 'master'
user = 'sa'
pw = 'Z'
#x=input('введите название базы',)
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+db+'; UID='+user+'; PWD='+pw+'')
cursor = conn.cursor()
cursor.execute('DROP DATABASE b_library')
cursor.execute('DROP DATABASE testDB2')
cursor.execute('DROP DATABASE testDB3')
#conn.commit()
conn.close()