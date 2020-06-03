FROM python:3.8.2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ /app
WORKDIR /app

CMD ["python", "main.py"]
