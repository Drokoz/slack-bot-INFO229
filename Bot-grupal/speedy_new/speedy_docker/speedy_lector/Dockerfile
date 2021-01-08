FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27018
ENV SLACK_TOKEN="bc4a0a2950f1a20bc38c1dc5c32facc2"
ENV SLACK_SIGNING_SECRET="bc4a0a2950f1a20bc38c1dc5c32facc2"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /speedy_lector

COPY ./speedy_lector.py /speedy_lector.py

CMD [ "python", "/speedy_lector.py" ]
