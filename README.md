# Face-Recognition-Flask-Web-App
Face recognition Flask web app using Raspberry Pi and Coral Edge TPU

Startボタンを押すと顔認識エンジンが起動。認識した画像はFlask Web App上で表示。

## アーキテクチャ

## ファイル構成
    .
    ├── Makefile
    ├── README.md
    ├── docker-compose.yml
    ├── app
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── src
    │   │   ├── config
    │   │   │   ├── __init__.py
    │   │   │   └── default.py
    │   │   ├── server
    │   │   │   └── __init__.py
    │   │   ├── run.py
    │   │   └── templates
    │   │       ├── index.html
    │   │       └── test.html
    │   └── uwsgi.ini
    └── nginx
        ├── log
        │   └── ...
        ├── Dockerfile
        └── nginx.conf
    
## コマンド(ver.make)
    #  実行
    $ make run
    #  停止
    $ make stop

## コマンド(other)
    #  実行
    $ docker-compose up -d
    #  停止
    $ docker-compose down