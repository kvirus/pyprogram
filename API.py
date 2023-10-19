import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



# import time
#
#
# file1 = open("D:\\tmp\\it151.txt", "r")
# while True:
#     line = file1.readlines()
#     x=0
#     y = 1
#     for i in line:
#         x=x+1
#         y = y + 1
#         if x % 2 != 0:
#             print(i.strip())
#             time.sleep(2)
#         else:
#             print(i.strip())
#             time.sleep(2)
#
#     time.sleep(1)
#     #print(line.strip())
