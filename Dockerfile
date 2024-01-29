FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 2947

LABEL name="dummy_gps_api"

CMD ["uvicorn", "dummy_gps_api:app", "--host", "0.0.0.0", "--port", "2947"]
