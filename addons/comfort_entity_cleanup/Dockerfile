ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Tambah Python
RUN apk add --no-cache python3 py3-pip bash

# Copy script ke container
COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
