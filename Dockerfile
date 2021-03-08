FROM python:3.8-slim-buster

RUN pip install -U pip && pip install acdh-arche-pyutils tqdm

WORKDIR /opt

COPY sync.py sync.py

CMD ["python", "sync.py"]