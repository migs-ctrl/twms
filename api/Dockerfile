FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD uvicorn --proxy-headers --forwarded-allow-ips=* --reload main:app --host 0.0.0.0 --port 8000
