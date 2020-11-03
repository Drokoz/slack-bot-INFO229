FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1444629029761-1425284248550-KBSxJTntiJUtEERBZiXvq44w"
ENV SLACK_SIGNING_SECRET="bc4a0a2950f1a20bc38c1dc5c32facc2"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /speedy

COPY ./speedy.py /speedy.py
COPY ./speedybot_app.py /speedybot_app.py

CMD [ "python", "/speedybot_app.py" ]
