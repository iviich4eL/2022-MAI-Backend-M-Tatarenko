## Postgres
Установка Postgres:
```console
brew install postgresql
```
Запуск и остановка Postgres:
```console
brew services start postgresql
brew services stop postgresql
```

Создание пользователи и базы данных в Postgres:
```console
CREATE ROLE mai LOGIN PASSWORD '12345' CREATEDB;
CREATE DATABASE myapp WITH OWNER = mai;
```

```console
# psql -h localhost -d mydatabase -U myuser -p <port>
```

## Migrations
Создать миграцию:
```console
python3 manage.py makemigrations
```
Сделать миграцию:
```console
python3 manage.py migrate
```

Создание sql файла миграции:
```console
python3 manage.py sqlmigrate myapp 0001 > migration.txt
```

Проверить миграцию:
```console
python3 manage.py check
```

Показать миграции:
```console
python3 manage.py showmigrations myapp
```
```console
python3 manage.py shell
```

## Superuser

```console
python3 manage.py createsuperuser
```
