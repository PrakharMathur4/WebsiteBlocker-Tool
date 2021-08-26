import time
from datetime import datetime as dt

ip_localmachine = "127.0.0.1"
list = ["www.facebook.com", "www.instagram.com", "www.netflix.com", "www.hotstar.com", "facebook.com", "instagram.com"]
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
start_time = "09:0:0"
end_time = "11:0:0"

date_today = dt.now()
current_time = date_today.strftime("%H:%M:%S ")
print(current_time)

#hosts file will have mappping of domain and ip address.
while True:
    if start_time<=current_time and current_time<=end_time:
        print("Working Hours!")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in list:
                if website in  content:
                    pass
                else:
                    file.write(ip_localmachine+" "+website+"\n")

    else:
        print("Non-Working Hour!")

        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in list):
                    file.write(line)

                file.truncate()

    time.sleep(20)         # every 20 secs it will print whether it is working or non working hours
