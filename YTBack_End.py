import sys
import os
import json
import commands

def find(link):
    os.system("youtube-dl " + link)
    os.system("youtube-dl --list-formats " + link)
    print ("sys.argv")
    print sys.argv
    print(commands.getstatusoutput("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'"))
    return

link = "https://www.youtube.com/watch?v=JoTMpxG8Zwc"

find(link)