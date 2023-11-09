# Добро пожаловать на реализацию проекта "Табло Теннисного Мяча" #

#### Проект был реализован по ТЗ - https://github.com/zhukovsd/java-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####
#### Python версия ТЗ - https://github.com/zhukovsd/python-backend-learning-course/blob/main/Projects/TennisScoreboard/index.md ####

## Используемые технологии ##

## Описание проекта ##

## Запуск проекта ##
### Развернуть локально из Windows ###
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      1. DB_USER - логин
      2. DB_PASS - пароль
      3. DB_HOST - my_sql_db
4. Выполните команду docker-compose up

### Развернуть на сервере Linux ###
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      1. DB_USER - логин
      2. DB_PASS - пароль
      3. DB_HOST - my_sql_db
4. (Далее инструкция для Ubuntu 22.04) Нам нужно установить композ версии v2.23.0
5. <code>mkdir -p ~/.docker/cli-plugins/</code>
6. <code>curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose</code>
7. <code>chmod +x ~/.docker/cli-plugins/docker-compose</code>
8. Для проверки корректной установки введите <code>docker compose version</code>
9. Далее собираем образы и запускаем приложение при помощи команды <code>docker compose up</code>

#### Развернуть c помощью dockerfile ####
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Найдите файл ___".env_sample"___ и следуйте инструкциям ниже
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      1. DB_USER - логин
      2. DB_PASS - пароль
      3. DB_HOST - пропишите __ip-address вашего сервера__ - если вы деплоите на удаленный VDS 
      4. Или __127.0.0.1/host.docker.internal__ - если вы из локальной машины запускаете
4. Запустите вашу базу данных при помощи команды: (Отредактируйте юзера и пароль под данные в .env)
   - __Не используйте фигурные скобки в команде ниже__ 
   - <code>docker run --name test_db --rm -e MYSQL_ROOT_PASSWORD={Ваш пароль} -e MYSQL_DATABASE=Ball_Scoreboard_db -e MYSQL_USER={Ваше имя пользователя} -e MYSQL_PASSWORD={Ваш пароль} -d -p 3306:3306 mysql</code>
5. Сбилдите Dockerfile с помощью команды:
   - <code>docker build . -t tennis_ball_scoreboard_project_in_ubuntu</code>
6. Запустите контейнер при помощи только что созданного образа
   - <code>docker run --name my_server_ubuntu_container -it -p 8080:80 tennis_ball_scoreboard_project_in_ubuntu</code>
7. Переходите по адресу вашего сервера:8080 и проверяйте работу
