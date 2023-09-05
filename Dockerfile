# Команда для билда - docker build . -t main_image_app
# Команда для запуска - docker run --name my_server_machine -it -p 8080:80 -v откуда:куда id_images

FROM tecktron/python-waitress:latest

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mv wsgi.py wsgi1.py
RUN mv main.py wsgi.py
