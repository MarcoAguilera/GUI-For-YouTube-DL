import os
#from YTBack_End import store_info
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

info = "" 

@app.route("/")
def mainPage():
    return render_template("mainscreen.html")
    
@app.route("/", methods=['POST'])
def mainPagePost():
    url = request.form['url']
    option = request.form['select']
    print (url)
    print (option)
    global info
   # info = store_info(url)
    print ("*******************************************************************")
    print info
    return redirect(url_for('mainPage'))
#for testing purposes
@app.route("/text")
def textreader():
    return render_template("readtext.html")
##############################3
    
@app.route("/option")
def optionPage():
    return render_template("select.html")
    
@app.route("/option", methods=['POST'])
def optionPagePost():
    html = request.form.get('videoQuality')
    return redirect(url_for('mainPage'))

    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
        )