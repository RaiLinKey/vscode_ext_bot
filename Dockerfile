FROM python:3.12.4-slim

WORKDIR /app

COPY app/ .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8080

CMD ["python3", "-m", "main"]
