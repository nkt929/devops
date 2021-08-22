# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install Flask pytz
EXPOSE 5000
COPY . .
CMD ["flask", "run"]