# Добро пожаловать на реализацию проекта "Табло Теннисного Мяча" #

#### Проект был реализован по ТЗ - https://github.com/zhukovsd/java-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####
#### Python версия ТЗ - https://github.com/zhukovsd/python-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####

## Используемые технологии ##
- Python3
- uwsgi: В качестве Веб сервера
- dotenv: Для переменных окружения
- pytest: Тестирование
- VDS Linux Ubuntu
- Docker и Docker-Compose: для развертывания и деплоя
- Jinja2: в качестве Шаблонизатора
- HTML and CSS: для оформления
- alembic: для миграций
- sqlalchemy: ORM для манипуляций с БД
- MySQL: в качестве базы данных
- Архитектурный паттерн MVCS

## Описание и компоненты проекта ##
Основная идея проекта - создать клиент-серверное приложение для подсчета очков в теннисе.
#### Целью проекта являлось: ####
- Получение практического опыта с html & css без использования фреймворков
- Попрактиковаться с шаблонизатором 
- Поработать с инструментами тестирования 
- Познакомиться с архитектурным паттерном MVCS
- Познакомиться и получить практический опыт работы с ORM и миграциями
- Закрепить предыдущий и получить опыт новый опыт при работе и настройке с веб-сервером WSGI
### Компоненты проекта ###
#### Главная страница матча ####
Содержит две кнопки 
1. Страница нового матча
2. Список сыгранных матчей
#### Страница подсчета матча ####
После нажатия на кнопку начала нового матча вы попадаете на страницу создания нового матча для подсчета.  
Затем после ввода имен игроков переходите на страницу подсчета матча которая отображает реализованную логику приложения.  
И по окончанию матча добавляет результаты в таблицу сыгранных матчей сразу же переходя к ним.
#### Страница сыгранных матчей ####
Состоит из таблицы с именами игроков созданный с помощью блочной верстки.  
Поиска - который может фильтровать сыгранные матчи по именам.  
И динамической пагинации.
## Запуск проекта ##
### Развернуть локально из Windows ###
##### P.S. Подразумевается что Docker-Compose установлен в вашу систему. #####
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      - DB_USER - логин
      - DB_PASS - пароль
      - DB_HOST - my_sql_db
      - YOUR_IP_ADDR - localhost или 127.0.0.1
   3. (ЛИБО) Создайте файл __".env"__
      - SQL_DRIVER=mysql+mysqlconnector 
      - DB_USER=Ваше имя пользователя
      - DB_PASS=Ваш Пароль
      - DB_HOST=my_sql_db 
      - #DB_HOST=host.docker.internal 
      - #DB_HOST=127.0.0.1 
      - #DB_HOST=Ваш IP 
      - DB_PORT=3306 
      - DB_NAME=Ball_Scoreboard_db 
      - YOUR_IP_ADDR=Ваш IP
4. Выполните команду <code>docker compose up</code>
5. Открываете браузер и переходите на localhost:8080

### Развернуть на сервере Linux Ubuntu 22.04 ###
##### P.S. Подразумевается что Docker-Compose НЕ установлен в вашу систему. #####
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Перейдите в папку с проектом при помощи <code>cd Tennis_Ball_Scoreboard</code>
4. Запустите виртуальное окружение в папке с проектом с помощью команд:
   - <code>python3 -m venv venv</code>
   - <code>source venv/bin/activate</code>
5. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД и IP адрес который вы будете использовать для перехода по ссылкам
      - DB_USER - логин
      - DB_PASS - пароль
      - DB_HOST - my_sql_db
      - YOUR_IP_ADDR - IP вашего сервера
   3. (ЛИБО) Создайте файл __".env"__
      - SQL_DRIVER=mysql+mysqlconnector 
      - DB_USER=Ваше имя пользователя
      - DB_PASS=Ваш Пароль
      - DB_HOST=my_sql_db 
      - #DB_HOST=host.docker.internal 
      - #DB_HOST=127.0.0.1 
      - #DB_HOST=Ваш IP 
      - DB_PORT=3306 
      - DB_NAME=Ball_Scoreboard_db 
      - YOUR_IP_ADDR=Ваш IP
6. (Далее инструкция для Ubuntu 22.04) Нам нужно установить docker compose версии v2.23.0
7. <code>mkdir -p ~/.docker/cli-plugins/</code>
8. <code>curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose</code>
9. <code>chmod +x ~/.docker/cli-plugins/docker-compose</code>
10. Для проверки корректной установки введите <code>docker compose version</code>
11. Далее собираем образы и запускаем приложение при помощи команды <code>docker compose up</code>
12. И переходим по адресу вашего проекта

#### Развернуть c помощью dockerfile ####
##### P.S. Подразумевается что Docker установлен в вашу систему. #####
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Перейдите в папку с проектом при помощи <code>cd Tennis_Ball_Scoreboard</code>
4. Запустите виртуальное окружение в папке с проектом с помощью команд:
   - <code>python3 -m venv venv</code>
   - <code>source venv/bin/activate</code>
5. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      - DB_USER - логин
      - DB_PASS - пароль
      - DB_HOST - пропишите __ip-address вашего сервера__ - если вы деплоите на удаленный VDS 
      - Или __127.0.0.1/host.docker.internal__ - если вы из локальной машины запускаете
   3. (ЛИБО) Создайте файл __".env"__
      - SQL_DRIVER=mysql+mysqlconnector 
      - DB_USER=Ваше имя пользователя
      - DB_PASS=Ваш Пароль
      - #DB_HOST=my_sql_db 
      - #DB_HOST=host.docker.internal 
      - #DB_HOST=127.0.0.1 
      - DB_HOST=Ваш IP 
      - DB_PORT=3306 
      - DB_NAME=Ball_Scoreboard_db 
      - YOUR_IP_ADDR=Ваш IP
6. Запустите вашу базу данных при помощи команды: (Отредактируйте юзера и пароль под данные в .env)
   - __Не используйте фигурные скобки в команде ниже__ 
   - <code>docker run --name test_db --rm -e MYSQL_ROOT_PASSWORD={Ваш пароль} -e MYSQL_DATABASE=Ball_Scoreboard_db -e MYSQL_USER={Ваше имя пользователя} -e MYSQL_PASSWORD={Ваш пароль} -d -p 3306:3306 mysql</code>
7. Сбилдите Dockerfile с помощью команды:
   - <code>docker build . -t tennis_ball_scoreboard_project_in_ubuntu</code>
8. Запустите контейнер при помощи только что созданного образа
   - <code>docker run --name my_server_ubuntu_container -it -p 8080:80 tennis_ball_scoreboard_project_in_ubuntu</code>
9. Переходите по адресу вашего сервера:8080 и проверяйте работу
