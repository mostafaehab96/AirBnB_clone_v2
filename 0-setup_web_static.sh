#!/usr/bin/env bash
#Installs nginx and deploy web_static

my_html="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
my_configs="

	server { 
		
		root /data/web_static/current;

		location /hbnb_static {
			alias /data/web_static/current/;
		}
	}
"
#sudo apt-get -y update
#sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
echo "$my_html" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '/^http {/r /dev/stdin' /etc/nginx/nginx.conf <<< "$my_configs"
sudo sed -i '/sites-enabled/d' /etc/nginx/nginx.conf
sudo nginx -s reload
