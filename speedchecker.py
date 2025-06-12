import speedtest

st = speedtest.Speedtest()
download = st.download() / 1024 / 1024
upload = st.upload() / 1024 /1024
ping = st.results.ping

print(f"Download speed is: {download:.2f} Mbps")
print(f"Upload speed is: {upload:.2f} Mbps")
print(f"Ping is: {ping:.2f} ms")
