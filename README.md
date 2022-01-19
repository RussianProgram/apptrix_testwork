# Тестовое задание для Apptrix

## Задачи:

1) [Создать модель участников. У участника должна быть аватарка, пол, имя и фамилия, почта.](https://github.com/RussianProgram/apptrix_testwork/commit/cab0d874f36d0768b35b72129ebbda05cb3dda0f)

2) [Создать эндпоинт регистрации нового участника: /api/clients/create (не забываем о пароле и совместимости с авторизацией модели участника)](https://github.com/RussianProgram/apptrix_testwork/commit/fdda6d0938653bfd76836bb2d00e00a1219fa7d3)

3) [При регистрации нового участника необходимо обработать его аватарку: наложить на него водяной знак (в качестве водяного знака можете взять любую картинку).](https://github.com/RussianProgram/apptrix_testwork/commit/41d5564f7207440c263ba63626d1d512f354efbd)

4) [Создать эндпоинт оценивания участником другого участника: /api/clients/{id}/match. В случае, если возникает взаимная симпатия, то ответом выдаем почту клиенту и отправляем на почты участников: «Вы понравились <имя>! Почта участника: <почта>».](https://github.com/RussianProgram/apptrix_testwork/commit/0273bab80a8bb9b6bc4bd130df3cae279e5f508c)

5) [Создать эндпоинт списка участников: /api/list. Должна быть возможность фильтрации списка по полу, имени, фамилии. Советую использовать библиотеку Django-filters.](https://github.com/RussianProgram/apptrix_testwork/commit/32bcb67b4e951520328bed750a34b5afdca17baa)

6) [Реализовать определение дистанции между участниками. Добавить поля долготы и широты. В api списка добавить дополнительный фильтр, который показывает участников в пределах заданной дистанции относительно авторизованного пользователя. Не забывайте об оптимизации запросов к базе данных
https://en.wikipedia.org/wiki/Great-circle_distance](https://github.com/RussianProgram/apptrix_testwork/commit/a1606c985f24df564d88226d48d95c6efb9db453)

7) [Задеплоить проект на любом удобном для вас хостинге, сервисах PaaS (Heroku) и т.п. Должна быть возможность просмотреть реализацию всех задач. Если есть какие-то особенности по тестированию, написать в Readme. Там же оставить ссылку/ссылки на АПИ проекта]()

# HOW TO:
## Как запустить
### Клонируем
```
git clone https://github.com/RussianProgram/apptrix_testwork.git
```
### Первоначальная установка 
```
cd apptix_testwork
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```
Создаём супер-юзера с именем admin и паролем admin.

# API DOCUMENTATION:
### CLIENTS LIST (GET)
```shell
curl --location --request GET http://localhost:8000/api/clients/
```
### CREATE CLIENT (POST)
```shell
curl --data "username=somename&password=somepass&password2=somepass&email=email&first_name=name&last_name=name" http://localhost:8000/api/clients/
```
### CLIENT DETAIL (GET)
```shell
curl --location --request GET http://localhost:8000/api/clients/{client_id}/
```
### CLIENT UPDATE (PUT) 
#### Authentification only!
```shell
curl --data "{"sex":"F""}" http://localhost:8000/api/clients/{client_id}/
```
### CLIENT MATCH (GET)
#### Authentification only!
```shell
curl --location --request GET http://localhost:8000/api/clients/{client_id}/match/
```
