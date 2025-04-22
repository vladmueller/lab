FROM ubuntu:24.04
LABEL maintainer="Vladimir Müller <code@vladmueller.de>"

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential python3-pip python3-venv \
    && apt-get install -y libglib2.0-0 libglib2.0-dev libpango1.0-dev

ADD requirements.txt /

RUN python3 -m venv /venv

RUN /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install -r requirements.txt

WORKDIR /workdir

ENV PATH="/venv/bin:$PATH"

ENTRYPOINT ["make"]
