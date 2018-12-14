FROM python:3.6

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN chmod +x ./wait_for_mysql.sh

CMD python app.py
