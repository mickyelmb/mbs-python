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
