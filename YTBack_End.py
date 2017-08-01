import subprocess

def store_info(link):
    
    process = subprocess.Popen(['youtube-dl', '--list-formats', str(link)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print("PRINTING")
    file = open("formats.txt", "w+")
    file.write(out)
    file.close()
    return out

