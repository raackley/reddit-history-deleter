FROM python:3-alpine

LABEL maintainer="raackley@protonmail.com"

ADD src/ .

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "reddit-history-deleter.py"]