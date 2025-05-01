# Dockerfile for centralized Flask app with HTML
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY templates/ templates/

CMD ["python", "app.py"]
