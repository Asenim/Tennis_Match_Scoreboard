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
      1. DB_USER - логин и DB_PASS - пароль
4. Выполните команду docker-compose up

### Развернуть на сервере Linux ###
1. Перейдите в папку на вашем компьютере в которой должен находится проект
2. Используйте команду <code> git clone https://github.com/Asenim/Tennis_Ball_Scoreboard.git </code> для клонирования проекта
3. Перейдите в файл ___".env_sample"___ и следуйте инструкциям 
   1. Переименуйте файл ___".env_sample"___ в ___".env"___ 
   2. Пропишите данные вашей БД
      1. DB_USER - логин и DB_PASS - пароль
4. (Далее инструкция для Ubuntu 22.04) Нам нужно установить композ версии v2.23.0
5. <code>mkdir -p ~/.docker/cli-plugins/</code>
6. <code>curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose</code>
7. <code>chmod +x ~/.docker/cli-plugins/docker-compose</code>
8. Для проверки корректной установки введите <code>docker compose version</code>
9. Далее собираем образы и запускаем приложение при помощи команды <code>docker compose up</code>
