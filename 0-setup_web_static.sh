#!/usr/bin/env bash
# Web servers preparation script
# Install nginx on server
sudo apt-get -y update
sudo apt-get -y install nginx
# Create the folder /data/web_static/releases/test if it doesn’t already exist
if [ ! -d /data/web_static/releases/test/ ]; then
sudo mkdir -p /data/web_static/releases/test/
fi;
# Create the folder /data/web_static/shared/ if it doesn’t already exist
if [ ! -d /data/web_static/shared/ ]; then
sudo mkdir -p /data/web_static/shared/
fi;
# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sfn /data/web_static/releases/test /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown ubuntu. -R /data
# Update the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
sudo sed -i '20i location /hbnb_static/ {\nalias /data/web_static/current/;\nautoindex off;\n}' /etc/nginx/sites-available/default
# start service
sudo service nginx restart
