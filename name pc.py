import platform
import os
import getpass, socket

user = getpass.getuser()
print(getpass.getuser())
domain = os.environ['userdomain']
print(domain)
#ip = socket.gethostbyname(socket.getfqdn())
#print(ip)

pc_name = platform.node()
print (pc_name)
save_name = open('//it15/tmp/allpc/'+pc_name + '.txt',"a+")
save_name.write('\n' + 'Пользователь: ' + domain + '\\' +user +'\n')
save_name.write('Имя компьютера: ' + pc_name + '\n')
#save_name.write('Ip адрес: ' + ip + '\n')
save_name.write('-------------------------------------------------')
save_name.close()