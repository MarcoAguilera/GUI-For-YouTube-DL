import subprocess
class Media(object):
    
    #Uses this constructor to instanciate an object when a link is entered
    def __init__(self,link):
        self.link = link
    
    #After a link has been set, use this function to gather information about the link    
    def set_info(self):
        self.process = subprocess.Popen(['youtube-dl', '--list-formats', self.link], stdout=subprocess.PIPE)
        self.out, self.err = self.process.communicate()
        file = open("formats.txt", "w+")
        file.write(self.out)
        file.close()
    
    #Used to store format code for later use    
    def set_format_code(self,code):
        self.format_code = code
    
    #Used to download on to computer
    def download_media(self):
        subprocess.Popen(['youtube-dl', '-f', str(self.format_code), self.link])
        