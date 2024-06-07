FROM python:3.11-alpine as base
RUN apk add git make

FROM base as app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
COPY src /app
WORKDIR /app

## LINTING
FROM app as lint
RUN pip install flake8
COPY Makefile .
CMD ["make", "lint"]

## TESTING
FROM app as test
COPY Makefile .
RUN pip install pytest
CMD ["make", "test"]

FROM app
CMD ["python", "cli.py"]
