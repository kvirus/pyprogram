import speedtest

st = speedtest.Speedtest()

while True:
    down_speed = st.download()
    print (down_speed / (2**20))

    up_speed = st.upload()
    print(up_speed/ (2**20))

