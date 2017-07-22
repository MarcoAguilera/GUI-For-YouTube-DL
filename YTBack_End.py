import subprocess

def get_info(link):
 
    process = subprocess.Popen(['youtube-dl', '--list-formats', str(link)], stdout=subprocess.PIPE)
    out, err = process.communicate()
    
    return out    
