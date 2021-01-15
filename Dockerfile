FROM python:3-slim-buster

LABEL maintainer="raackley@protonmail.com"

ADD src/ .

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "reddit-history-deleter.py"]