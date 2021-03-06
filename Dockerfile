FROM ubuntu:latest 

ENV PYTHONNUNBUFFERD 1

RUN set -ex \
    && RUN_DEPS=" \
	libpcre3 \
        mime-support \ 
    " \
    && seq 18 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /wku_sims
WORKDIR /wku_sims
COPY requirements.txt /wku_sims/

RUN set -ex \
    && BUILD_DEPS=" \
        build-essential \
        libpcre3-dev \
        libpq-dev zlib1g zlib1g-dev libjpeg-dev python3-dev \ 
	python3 python3-pip \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS 
RUN ln -fs /usr/share/zoneinfo/America/Chicago /etc/localtime

RUN apt-get install tzdata

RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN pip3 install -U pip setuptools wheel 

RUN pip3 install --no-cache-dir -r requirements.txt   

RUN apt-get -y install python3-numpy python3-pandas python3-matplotlib

COPY . /wku_sims/

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=wku_sims.settings

ENV UWSGI_WSGI_FILE=/wku_sims/wku_sims/wsgi.py

ENV UWSGI_HTTP=:8000 USGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_UID=1000 UWSGI_GID=2000 UWSGT_LAZY_APPS=3 UWSGI_WSGI_ENV_BEHAVIOR=holy

ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

ENV UWSGI_STATIC_MAP="/static/=/wku_sims/static/"

CMD ["/usr/local/bin/uwsgi", "--show-config"]

