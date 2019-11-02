"""
This python script can be used to block websites at working hours.
By default this script will now block facebook.com and working hours are  08:00- 16:00.
Windows must be installed at c drive.
**Must be run as an Administrator**
"""

import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"] #blacklist, more sites can be added here

while True:
    #Check if it is Working hours
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:    #check if website is already in list
                if website in content:      #so I don't write it again
                    pass
                else:
                    file.write("\n" + redirect + " " + website + "\n")
    else:
        #I can't delete lines from host file so I will a new one without
        #the blocked sites from my website_list
        with open(hosts_path,'r+') as file:
            content=file.readlines() #this will produce a list with all the lines, each item will be a line of the host file
            file.seek(0) #place pointer before the first character, because now it is in the end of host file
            for line in content:
                if not any(website in line for website in website_list): #if a website of my list is not in the line
                #the line will be pasted to the hostfile
                    file.write(line)
            file.truncate() #clear everything after pointer, otherwise the content will be pasted continuously
        print("Free Time")

    time.sleep(5) #state will be checkd every 5 seconds
