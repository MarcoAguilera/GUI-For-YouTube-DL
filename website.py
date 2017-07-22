import os
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("mainscreen.html")
    
@app.route("/", methods=['POST'])
def mainPagePost():
    html = request.form['html']
    print (html)
    return redirect(url_for('optionPage'))
    
@app.route("/option")
def optionPage():
    return render_template("select.html")
    
@app.route("/option", methods=['POST'])
def optionPagePost():
    print ('in post')
    html = request.form.get('videoQuality')
    print ("got it")
    print (str(html))
    return redirect(url_for('mainPage'))
    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )
    