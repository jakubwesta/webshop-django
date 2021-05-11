FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /webshop
WORKDIR /webshop
ADD requirements.txt /webshop/
RUN pip install -r requirements.txt
ADD . /webshop/