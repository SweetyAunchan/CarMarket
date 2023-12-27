# start by pulling the python image
ARG CODE_VERSION=20.04 

FROM ubuntu:${CODE_VERSION}
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /et
RUN apt update -y
RUN apt-get -y install python3 python3-pip nano sudo
RUN pip3 install --upgrade pip setuptools
RUN apt-get install -y locales locales-all

RUN apt-get -y install poppler-utils
RUN apt-get install libpoppler-dev

RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        make \
        automake \
        autoconf \
        bzip2 \
        unzip \
        wget \
        libtool \
        git \
        subversion \
        python2.7 \
        python3 \
        python3-pip \
        zlib1g-dev \
        gfortran \
        ca-certificates \
        patch \
        ffmpeg \
        tesseract-ocr \
    vim && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/src

COPY requirements.txt ./
COPY . .
RUN pip3 install -r requirements.txt


ENV TESSDATA_PREFIX /app/src/tessdata
CMD ["python3", "-u", "./app.py", "&"]