from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

# python virtual command C:\Python code\WebBrowser\mysite>python -m venv virtual
# C:\Python code\WebBrowser\mysite\virtual\Scripts> pip install flask
# You should create the virtual environment before you create a web app
#https://mickyelmb.herokuapp.com/ | https://git.heroku.com/mickyelmb.git
"""
C:\Python
code\WebBrowser\mysite(master)
 heroku git:remote - -app mickyelmmb
set git remote heroku to
https: // git.heroku.com / mickyelmmb.git

C:\Python
code\WebBrowser\mysite(master)
git push heroku master
git config --global user.email "email username"
git config --global user.name " username "                                                
"""