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
    
@app.route("/options")
def optionPage():
    return render_template("optionPage.html")
    
#@app.route("/option", Methods=["POST"])
#def optionPagePost():
    #
    #
    #
    #
    
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )
    
    
    