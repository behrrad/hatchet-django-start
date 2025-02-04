FROM python:3.10-slim

WORKDIR /app

COPY app/hatchet/requirements.txt .
RUN pip install -r requirements.txt

COPY app/hatchet/worker.py .

CMD ["python", "worker.py"] 