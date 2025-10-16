ARG BUILD_FROM=homeassistant/amd64-base-python3
FROM ${BUILD_FROM}

WORKDIR /app
COPY run.py /app/run.py

RUN pip install requests

CMD ["python3", "/app/run.py"]
