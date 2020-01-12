from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


#  flaskの設定
app = Flask(__name__)
app.config.from_object('config.default')

bootstrap = Bootstrap(app)

