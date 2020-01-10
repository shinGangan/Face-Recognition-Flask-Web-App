#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#   Updata History
#   January  11  02:00, 2020 (Thu)
#------------------------------------------------------------
#   Raspberry Pi・Coral Edge TPU・Flask
#   ラズパイで顔検出を行い、Flask Web App上で表示させる
#------------------------------------------------------------

#  flask関係
from flask import Flask, render_template, requests
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/hello")
def hello():
    return "Hello world!!"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def results():
    return "results"

if __name__ == "__main__":
    app.run()