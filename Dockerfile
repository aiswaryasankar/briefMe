# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Create app directory
WORKDIR /app

# Install production dependencies.
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app