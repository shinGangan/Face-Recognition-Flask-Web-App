#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#   Updata History
#   January  12  03:00, 2020 (Sun)
#------------------------------------------------------------
#   Raspberry Pi・Coral Edge TPU・Flask
#   ラズパイで顔検出を行い、Flask Web App上で表示させる
#------------------------------------------------------------

from server import app

#@app.route("/")
#def index():
#    return "Hello World!!"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()