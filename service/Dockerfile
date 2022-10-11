FROM python:3.9

ENV PYTHONUNBFFERED 1

WORKDIR /app

COPY requirements.txt /app


RUN pip install -r requirements.txt

COPY app /app

CMD python app.py

