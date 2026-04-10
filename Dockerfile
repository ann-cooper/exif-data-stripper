FROM python:3.12.12-slim-bookworm

RUN set -ex \
    && mkdir /code \
    && groupadd -g 999 appuser \
    && useradd -r -d /code -u 999 -g appuser appuser

WORKDIR /code
COPY . /code

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install setuptools wheel \
    && pip install -r requirements.txt \
    && chown -R appuser:appuser -R /code \
    && pip install . \
    && apt-get autoremove -y \
    && apt-get clean
USER appuser

ENTRYPOINT ["python", "src", "exif_util", "cli.py"]
