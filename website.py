import os
#from YTBack_End import store_info  MARCO dont forget to include the functions
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
    print ("*******************************************************************")
    print (url)
    print (option)
    print ("*******************************************************************")
    #-----------------------------------------------------------#
    #marco
    #can you add some functions here to download the best audio/video depending on the input?
    if(option == 'audio'):
        print ('mp3')
    else:
        print ('video')
    #instead of te print tatement just call your function and use the url variable as the parameter
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