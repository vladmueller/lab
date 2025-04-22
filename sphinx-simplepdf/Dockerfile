FROM ubuntu:24.04
LABEL maintainer="Vladimir Müller <code@vladmueller.de>"

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y --no-install-recommends make python3-pip python3-venv weasyprint \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /

RUN python3 -m venv /venv

RUN /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

WORKDIR /workdir

ENV PATH="/venv/bin:$PATH"

ENTRYPOINT ["make"]
