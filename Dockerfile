FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget

RUN mkdir -p dataset_asi && \
    wget https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv -O dataset_asi/CollegeDistance.csv

COPY scripts/prepare_request.py /app/scripts/prepare_request.py

COPY dataset_asi /app/dataset_asi

COPY flask_api.py /app
COPY optimised_model.pkl /app

CMD ["python", "flask_api.py"]
