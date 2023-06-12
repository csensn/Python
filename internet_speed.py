import speedtest

speed = speedtest.Speedtest()
download_speed = speed.download()
kb = 1024*download_speed
mb = 1024*kb
print("Your Download speed is", mb)

upload_speed = speed.upload()
print("Your Upload speed is", upload_speed)

# def bytes_to_mb(bytes):
#   KB = 1024 # One Kilobyte is 1024 bytes
#   MB = KB * 1024 # One MB is 1024 KB
#   return int(bytes/MB)
#
# download_speed = bytes_to_mb(speed.download())
# print("Your Download speed is", download_speed, "MB")