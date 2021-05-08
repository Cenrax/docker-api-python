FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel 
RUN pip install gunicorn uvloop httptools

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
COPY /service/ /app
# SUPER RUN
# EXPOSE THE DOCKER PORT 
ENTRYPOINT /usr/local/bin/gunicorn main:app  -b 0.0.0.0:80 -w 4 -k uvicorn.workers.UvicornWorker  --chdir /app --access-logfile "$ACCESS_LOG"