import os

name = open('c:\\intel\\name.txt','r')
line=name.readlines()
for nam in line:
    command3 = ("cd c:\PSTools & PsExec \\\{} -u pp.local\\bka -p J -s \\\it15\\tmp\install.cmd".format(nam))
    print(command3)
#print(command3)
#res = os.system(command3)
#print("Returned Value: ", res)
