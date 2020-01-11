NAME=flask_raspi

run:
	docker-compose build --no-cache
	docker-compose up -d

stop:
	docker-compose down
#	docker stop ${NAME}_uwsgi_1 ${NAME}_nginx_1
#	docker rm ${NAME}_uwsgi_1 ${NAME}_nginx_1

stoo_rm:
	docker-compose down --rmi all --volumes