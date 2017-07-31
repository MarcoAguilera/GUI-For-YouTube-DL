import os
from YTBack_End import get_info
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

info = "" 

@app.route("/")
def mainPage():
    return render_template("mainscreen.html")
    
@app.route("/", methods=['POST'])
def mainPagePost():
    url = request.form['url']
    print (url)
    global info
    info = get_info(url)
    print ("*******************************************************************")
    print info
    return redirect(url_for('optionPage'))
    
@app.route("/option")
def optionPage():
    return render_template("select.html" , display_info = info)
    
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