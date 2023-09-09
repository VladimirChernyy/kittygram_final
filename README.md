#  Проект «Kittygram»

## Описание проекта:

Проект Kittygram позволяет пользователям поделиться своим пушистым счастьем и рассказать о его достижениях!


## В проекте были использованы технологии:
* #### Django REST
* #### Python 3.9
* #### Gunicorn
* #### Nginx
* #### JS
* #### Node.js
* #### PostgreSQL
* #### Docker

## Попробовать демо-версию:
* [Kittygram](https://ya-kittygram.ddns.net)
---

## Как запустить проект:

 Настраиваем Docker
``` 
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin;
``` 
Переходим в директорию проекта.
``` 
cd kittygram_final/
``` 
Генерируем новый секретный ключ Django

```
sudo docker compose -f docker-compose.production.yml exec backend python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Создаем файл .env, в котором нужно указать данные

``` 
sudo nano .env
```
Добавьте в файл .env код  

```
DJANGO_KEY=<Сгенерированный_ключ>
POSTGRES_DB=<Желаемое_имя_базы_данных>
POSTGRES_USER=<Желаемое_имя_пользователя_базы_данных>
POSTGRES_PASSWORD=<Желаемый_пароль_пользователя_базы_данных>
DB_HOST=db
DB_PORT=5432
```
Далее выполняем последовательно:

Загрузите images
```
sudo docker compose -f docker-compose.production.yml pull
```
Остановите и удалите контейнеры 
```
sudo docker compose -f docker-compose.production.yml down
```
Соберите и запустите контейнеры в фоновом режиме
```
sudo docker compose -f docker-compose.production.yml up -d
```
Примените миграции
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```
Соберите статику
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```
Скопируйте статику в том
```
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collect_static/. /static_backend/static/
```
Создайте суперпользователся
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
```



Устанавливаем NGINX
```
sudo apt install nginx -y
```
Запускаем NGINX
```
sudo systemctl start nginx
```
Настраиваем firewall
```
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
```
Включаем firewall
```
sudo ufw enable
```
Откройте конфигурационный файл NGINX
```
sudo nano /etc/nginx/sites-enabled/default
```
Удалите из него все и напишите новые настройки
```
server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_set_header HOST $host;
        proxy_pass http://127.0.0.1:9000;

    }
}
```

Проверяем корректность настроек
```
sudo nginx -t
```
Запускаем NGINX
```
sudo systemctl start nginx
```

Настройте HTTPS


Установите пакетный менеджер snap.
```
sudo apt install snapd
```
Установите и обновите зависимости для пакетного менеджера snap.
```
sudo snap install core; sudo snap refresh core
```
Установите пакет certbot.
```
sudo snap install --classic certbot
```
Создайте ссылку на certbot в системной директории, чтобы у пользователя с правами администратора был доступ к этому пакету.
sudo ln -s /snap/bin/certbot /usr/bin/certbot

Получите сертификат 
```
sudo certbot --nginx
```
Перезапустите NGINX
```
sudo systemctl reload nginx
```



![main.yml](https://github.com/vladimirchernyy/kittygram_final/actions/workflows/main.yml/badge.svg)

## Над проектом работал:
* [Vladimir Chernyy](https://github.com/VladimirChernyy)