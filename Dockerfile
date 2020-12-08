FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE "5000:5000"

ENV FLASK_APP="main.py"

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]

