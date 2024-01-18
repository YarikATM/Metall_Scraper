FROM python:3.10 as builder
LABEL authors="yaroslav"

COPY . .

RUN pip install -r /app/requirements.txt



CMD [ "python", "main.py" ]