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
4.  № Расписать № Создайте БД на основе образа MySql <code>https://hub.docker.com/_/mysql </code>
5. Создайте образ для запуска приложения на основе одного из Докерфайлов в директории приложения. 
   - P.S. Рекомендую с помощью Dockerfile_for_ubuntu
   - Команда для Билда: <code> docker build . -f Dockerfile_for_ubuntu -t Tennis_ball_scoreboard_project_in_ubuntu </code>
6.  № Расписать № Запустите контейнер с Базой данных на основе образа с БД 
7. № Расписать № Выполните миграции
8. Запустите контейнер с проектом 
   Команда для Запуска: <code> docker run --name my_server_ubuntu_container -it -p 8080:80 Tennis_ball_scoreboard_project_in_ubuntu </code>
9. Перейдите на localhost:указанный порт/по умолчанию 8080
### Развернуть на сервере Linux ###
