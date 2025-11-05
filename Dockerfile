FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn flask plotly scikit-learn

EXPOSE 8000
EXPOSE 5050

CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000"]
