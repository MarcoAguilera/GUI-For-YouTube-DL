import os
from YTBack_End import Store_Info  
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

info = "" 
current = Store_Info()

@app.route("/")
def mainPage():
    return render_template("mainscreen.html")
    
@app.route("/", methods=['POST'])
def mainPagePost():
    current.set_link(request.form['url'])
    current.set_option(request.form['select'])
    #-----------------------Test Purposes------------------------#
    print ("*******************************************************************")
    print (current.get_link())
    print (current.get_option())
    print ("*******************************************************************")
    #-----------------------------------------------------------#

    if(current.get_option() == 'audio'):
        current.download_best_audio()
    else:
        current.download_best_video()
        
    return redirect(url_for('mainPage'))
    
@app.route("/option")
def optionPage():
    return render_template("select.html")

    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
        )