
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/test.conf

#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart






# git clone https://github.com/GusievVM/stepic_web_project.git /home/box/web


#sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
sudo ln -sf hello.py /usr/local/lib/python2.7/hello.py
sudo mkdir /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test

sudo /etc/init.d/mysql restart﻿

cd ~/web/
sudo gunicorn -b 0.0.0.0:8080 hello:application &
cd ~/web/ask/
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &





#sudo /etc/init.d/gunicorn restart
