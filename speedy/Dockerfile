FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1444629029761-1425284248550-yG9HGBRwjIdlJxqaW1xDB1B0"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor

COPY ./nestorbot.py /nestorbot.py
COPY ./nestorbot_app.py /nestorbot_app.py

CMD [ "python", "/nestorbot_app.py" ]
