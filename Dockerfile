FROM python:3.10


COPY . .

RUN pip install -r /app/requirements.txt



CMD [ "python", "/app/main.py" ]