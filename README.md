# Face-Recognition-Flask-Web-App
Face recognition Flask web app using Raspberry Pi and Coral Edge TPU

Startボタンを押すと顔認識エンジンが起動。認識した画像はFlask Web App上で表示。

## アーキテクチャ

## ファイル構成
    .
    ├── run.sh
    ├── README.md
    ├── docker-compose.yml
    ├── app
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── src
    │   │   ├── run.py
    │   │   ├── templates
    │   │   │   ├── index.html
    │   │   │   └── test.html
    │   │   └── static
    │   │       └── images
    │   │           ├── img_before_xx.jpg
    │   │           └── img_after_xx.jpg
    │   └── uwsgi.ini
    └── nginx
        ├── Dockerfile
        └── nginx.conf
    
## コマンド(ver.make)

    #  実行
    $ make run
    #  停止
    $ make stop