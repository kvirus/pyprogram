import os

name = open('c:\\intel\\name.txt','r')

# while True:
#     line2 = name.readline()
#     print(line2.strip())

# закрываем файл
#name.close
while True:
    line = name.readline()
    if not line:
        break
    command3 = ("cd c:\PSTools & PsExec \\\{} -u pp.local\\bka -p pass -s \\\it15\\tmp\install.cmd".format(line.strip()))
    print(command3)
# for nam in line:
#     print(nam)
    #command3 = ("cd c:\PSTools & PsExec \\\{} -u pp.local\\bka -p J -s \\\it15\\tmp\install.cmd".format(nam))
    #print(command3)
#print(command3)

name.close
#res = os.system(command3)
#print("Returned Value: ", res)
