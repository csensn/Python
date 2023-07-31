import time

block_site = ["www.facebook.com", "www.instagram.com"]
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

print("What you want Choice options: \n 1. Site Block \n 2. Site Unlock")
choice = int(input("Enter Choice : "))

if choice == 1:
    print("Start blocking.....")

    with open(host_path,"r+") as host_file:
        content = host_file.read()
        for website in block_site:
            if website not in content:
                host_file.write(redirect + " " + website + "\n")
                print(f"{website} blocked...!")
            else:
                print(f"{website} already Blocked....!")
                pass
else:
    print("Start Unblocking.....")

    with open(host_path, "r+") as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        for lines in content:
            if not any(website in lines for website in block_site):
                host_file.write(lines)
        host_file.truncate()
        print(f"{block_site} Unblocked...!")
    time.sleep(3)
