from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Linux World!  <b>Hello</b> <img src='https://myimagest.blob.core.windows.net/myclwimage/my.jpg' />"
