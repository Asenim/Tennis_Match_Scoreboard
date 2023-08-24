FROM tecktron/python-waitress:latest

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mv wsgi.py wsgi1.py
RUN mv main.py wsgi.py
