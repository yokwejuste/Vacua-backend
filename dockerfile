FROM python:3.9.1-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install gunicorn
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/