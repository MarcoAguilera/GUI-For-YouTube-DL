import subprocess

def store_info(link):
    
    process = subprocess.Popen(['youtube-dl', '--list-formats', str(link)], stdout=subprocess.PIPE)
    out, err = process.communicate()
<<<<<<< HEAD
    return out    
=======
    print("PRINTING")
    file = open("formats.txt", "w+")
    file.write(out)
    file.close()
    return out
>>>>>>> c6db00f847a010625491a22bd6749cbfd78d3310

