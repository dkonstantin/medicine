apt-get -y install python3
apt-get -y install python3-setuptools
easy_install3 pip
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py demodata
python3 manage.py runserver 0.0.0.0:80
