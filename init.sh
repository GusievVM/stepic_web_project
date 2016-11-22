
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/test.conf

#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart







sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf hello.py /usr/local/lib/python2.7/hello.py
sudo mkdir /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

sudo gunicorn -b 0.0.0.0:8080 hello:application &

#sudo /etc/init.d/gunicorn restart
#﻿sudo /etc/init.d/mysql start﻿
