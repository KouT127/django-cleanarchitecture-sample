docker run -d \
  -v $PWD/db:/var/lib/mysql \
  -v $PWD/init:/docker-entrypoint-initdb.d \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_USER=django \
  -e MYSQL_PASSWORD=password \
  -e MYSQL_DATABASE=django_tutorial \
  -p 3306:3306 --name mysql mysql:5.7