FROM continuumio/miniconda3:latest

LABEL MAINTAINER="Yonatan Kashi"
LABEL GitHub=""
LABEL version="0.1"
LABEL description="Flask API docker container for resty app"

SHELL ["/bin/bash", "-c"]

WORKDIR /home/resty-api

COPY environment.yml ./

ADD app ./app

RUN conda env update -f environment.yml
RUN pip install kubernetes flask-log-request-id

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

CMD ["python", "-u", "./app/resty-api.py"]
