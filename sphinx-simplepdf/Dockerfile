FROM ubuntu:24.04
LABEL maintainer="Vladimir Müller <code@vladmueller.de>"

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential \
    && apt-get install -y python3-pip

ADD requirements.txt /

RUN pip3 install -r requirements.txt

WORKDIR /workdir

ENTRYPOINT ["make"]
