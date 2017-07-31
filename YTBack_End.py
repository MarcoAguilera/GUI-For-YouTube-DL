import sys
import os
import json
import commands

def find(link):
    os.system("youtube-dl " + link) # // this command is to download the video right away.. Not trying to do this yet.
    os.system("youtube-dl --list-formats " + link)
    info = sys.argv
  #  print sys.argv
   # print(commands.getstatusoutput("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'"))
    return info

new = find('https://www.youtube.com/watch?v=sgA7KIwKlOE')

#print (new)