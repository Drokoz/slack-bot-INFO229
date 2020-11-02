FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN=""

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /speedy

COPY ./speedy.py /speedy.py
COPY ./speedybot_app.py /speedybot_app.py

CMD [ "python", "/speedybot_app.py" ]
