# Команда для билда - docker build . -t tennis_ball_scoreboard_project_in_ubuntu
# Команда для запуска -
#   docker run --name my_server_ubuntu_container -it -p 8080:80 -v Путь_к_приложению_на_вашем_ПК:/app tennis_ball_scoreboard_project_in_ubuntu
# Команда для тестов -
#   docker run --name my_server_ubuntu_container2 --rm -it -p 8080:80 -v Путь_к_приложению_на_вашем_ПК:/app tennis_ball_scoreboard_project_in_ubuntu
# Основная команда для запуска контейнера с полностью готовым проектом -
#   docker run --name my_server_ubuntu_container -it -p 8080:80 tennis_ball_scoreboard_project_in_ubuntu

FROM ubuntu

WORKDIR /app

COPY . .

RUN apt update
RUN apt upgrade -y

RUN apt install python3 -y
RUN apt install pip -y

RUN pip install --upgrade pip
RUN pip install uwsgi
RUN pip install -r requirements.txt

RUN chmod -R +x /app
ENTRYPOINT ["./entrypoint.sh"]
