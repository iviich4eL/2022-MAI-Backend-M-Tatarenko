Установка nginx и gunicorn:

```console
brew install nginx
pip3 install gunicorn
```

Nginx:

```console
nginx -c /Users/mikhail/Documents/Code/Mai-Backend/lab2/nginx.conf
nginx -s reload
nginx -s stop
```

Gunicorn:
```console
gunicorn --workers=2 main:app
```

Тестирование:
```console
ab -n 10 -c 2 -t 1 -v 2 http://localhost/index.html
```