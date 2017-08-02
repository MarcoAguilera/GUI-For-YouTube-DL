import subprocess

class Store_Info(object):
    
    #Uses this constructor to instanciate an object when a link is entered
    def __init__(self):
        self.link = ""
        self.option = ""
    
    def set_link(self,link):
        self.link = link
    
    def set_option(self,option):
        self.option = option
    
    #After a link has been set, use this function to gather information about the link    
    def set_info(self):
        self.process = subprocess.Popen(['youtube-dl', '--list-formats', self.link], stdout=subprocess.PIPE)
        self.out, self.err = self.process.communicate()
        file = open("formats.txt", "w+")
        file.write(self.out)
        file.close()
        subprocess.Popen(['python', 'recipe-532908-1.py', 'formats.txt'])
    
    #Used to store format code for later use    
    def set_format_code(self,code):
        self.format_code = code
        
    def get_link(self):
        return self.link
        
    def get_option(self):
        return self.option
    
    #Used to download on to computer
    def download_specific_media(self):
        subprocess.Popen(['youtube-dl', '-f', str(self.format_code), self.link])
    
    def download_best_audio(self):
         subprocess.Popen(['youtube-dl', '-f', '139/140/bestaudio', self.link])
         
    def download_best_video(self):
        subprocess.Popen(['youtube-dl', '-f', '137/22/237/bestvideo', self.link])