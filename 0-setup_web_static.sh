#!/usr/bin/env bash
#Installs nginx for deployment of web_static

my_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

my_configs="
server {

	listen 80 default_server;
	root /data/web_static/current;

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
"
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/default
echo "$my_html" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/default_server/d' /etc/nginx/sites-available/default
sudo echo "$my_configs" >> /etc/nginx/sites-available/default
sudo service nginx restart
