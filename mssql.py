import pyodbc

#Параметры подключения
driver = 'DRIVER={SQL Server}'
server = '1cdev2'
#port = 'PORT=1433'
db = 'msdb'
user = 'sa'
pw = ''

conn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+db+'; UID='+user+'; PWD='+pw+'')