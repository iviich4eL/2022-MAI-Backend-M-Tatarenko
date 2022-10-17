python3 -m venv mai_backend_lab
source mai_backend_lab/bin/activate
deactivate

/Users/mikhail/Documents/Code/Mai-Backend/mai_backend_lab/bin/python3 -m pip install --upgrade pip


// lab2

# install gunicorn
pip3 install gunicorn


# 


# Docroot is: /opt/homebrew/var/www
# nginx will load all files in /opt/homebrew/etc/nginx/servers/

# echo alias vscode=\"/Applications/Visual\\ Studio\\ Code.app/contents/Resources/app/bin/code\" >> ~/.zshrc
# vscode /opt/homebrew/etc/nginx/

ls /opt/homebrew/etc/nginx/nginx.conf

# nginx
nginx -c /Users/mikhail/Documents/Code/Mai-Backend/lab2/nginx.conf
nginx -s stop

# gunicorn
gunicorn --workers=2 main:app

# test
ab -n 10 -c 2 -t 1 -v 2 http://localhost/index.html