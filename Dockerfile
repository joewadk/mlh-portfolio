FROM python:3.9-slim-buster

WORKDIR /mlh_portfolio

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0 

CMD ["flask", "run"]

EXPOSE 5000
