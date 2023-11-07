# Добро пожаловать на реализацию проекта "Табло Теннисного Мяча" #

#### Проект был реализован по ТЗ - https://github.com/zhukovsd/java-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####
#### Python версия ТЗ - https://github.com/zhukovsd/python-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####

## Используемые технологии ##

## Описание проекта ##

## Запуск проекта ##
### Развернуть локально из Windows ###
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Перейдите в файл ___".env_sample"___ и следуйте инструкциям 
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
   3. Для работы из докера обязательно пропишите host.docker.internal (Выставлено по умолчанию)
      - В противном случае: Закомментируйте host.docker.internal и раскомментируйте  127.0.0.1
4. Создайте и запустите БД на основе образа MySql <code>https://hub.docker.com/_/mysql </code>
   - Для этого введите <code> docker run --name имя_контейнера -e MYSQL_ROOT_PASSWORD=пароль -e MYSQL_DATABASE=имя_базы_данных -e MYSQL_USER=имя_пользователя_базы_данных -e MYSQL_PASSWORD=пароль -d -p 3306:3306 mysql </code>
   - P.S. Все данные берите из файла ___".env"___
5. Создайте образ для запуска приложения на основе одного из Докерфайлов в директории приложения. 
   - P.S. Рекомендую с помощью Dockerfile_for_ubuntu
   - Команда для Билда: <code> docker build . -f Dockerfile_for_ubuntu -t tennis_ball_scoreboard_project_in_ubuntu </code>
6. Если вы до этого остановили кониейнер с БД то - Запустите его при помощи команды:
   - <code>docker run имя_контейнера </code>
7. Выполните миграции:
   - Проверьте что у вас установлен python с помощью команды python
   - Установите alembic с помощью: <code> pip install alembic </code>
   - (Если папка migrations есть можете пропустить этот пункт) Выполните <code> alembic init migrations </code>
   - Создайте вашу первую миграцию <code> alembic revision --autogenerate -m"имя файла создаваемого файла" </code>
   - Выполните миграции с помощью <code> alembic upgrage head </code>
8. Запустите контейнер с проектом 
   Команда для Запуска: <code> docker run --name my_server_ubuntu_container -it -p 8080:80 Tennis_ball_scoreboard_project_in_ubuntu </code>
9. Перейдите на localhost:указанный порт/по умолчанию 8080

### Развернуть на сервере Linux ###
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Перейдите в файл ___".env_sample"___ и следуйте инструкциям 
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
   3. Для работы из докера обязательно пропишите host.docker.internal (Выставлено по умолчанию)
      - В противном случае: Закомментируйте host.docker.internal и раскомментируйте  127.0.0.1
4. Создайте и запустите БД на основе образа MySql <code>https://hub.docker.com/_/mysql </code>
   - Для этого введите <code> docker run --name имя_контейнера -e MYSQL_ROOT_PASSWORD=пароль -e MYSQL_DATABASE=имя_базы_данных -e MYSQL_USER=имя_пользователя_базы_данных -e MYSQL_PASSWORD=пароль -d -p 3306:3306 mysql </code>
   - P.S. Все данные берите из файла ___".env"___
5. Создайте образ для запуска приложения на основе одного из Докерфайлов в директории приложения. 
   - P.S. Рекомендую с помощью Dockerfile_for_ubuntu
   - Команда для Билда: <code> docker build . -f Dockerfile_for_ubuntu -t tennis_ball_scoreboard_project_in_ubuntu </code>
6. Если вы до этого остановили кониейнер с БД то - Запустите его при помощи команды:
   - <code>docker run имя_контейнера </code>
7. Выполните миграции из линукс:
   - Проверьте что у вас установлен python с помощью команды python3
   - Установите pip <code> apt install python-pip </code>
   - Установите alembic с помощью: <code> pip3 install alembic </code>
   - 
8. Запустите контейнер с проектом 
   Команда для Запуска: <code> docker run --name my_server_ubuntu_container -it -p 8080:80 Tennis_ball_scoreboard_project_in_ubuntu </code>
9. Перейдите на localhost:указанный порт/по умолчанию 8080