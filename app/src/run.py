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
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world!!"

@app.route('/h')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()