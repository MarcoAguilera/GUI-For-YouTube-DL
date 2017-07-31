import subprocess

<<<<<<< HEAD
def find(link):
    os.system("youtube-dl " + link) # // this command is to download the video right away.. Not trying to do this yet.
    os.system("youtube-dl --list-formats " + link)
    info = sys.argv
  #  print sys.argv
   # print(commands.getstatusoutput("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'"))
    return info

new = find('https://www.youtube.com/watch?v=sgA7KIwKlOE')

#print (new)
=======
def get_info(link):
 
    process = subprocess.Popen(['youtube-dl', '--list-formats', str(link)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    
    return out    
>>>>>>> e723c0fc1dc72d3001cb657ae354899331641722
