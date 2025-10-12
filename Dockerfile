ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:10.2.3
FROM ${BUILD_FROM}

COPY run.py /
RUN chmod a+x /run.py

CMD [ "python3", "/run.py" ]
