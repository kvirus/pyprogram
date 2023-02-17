from pythonping import ping
import speedtest
st = speedtest.Speedtest()

print(st.download())
#
# response_list = ping('192.168.0.1', size=40, count=2)
# print(response_list)