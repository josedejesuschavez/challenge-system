FROM python:3.9.1
RUN mkdir /code
COPY requirements.txt /code
WORKDIR /code
RUN pip install -r requirements.txt

ENV PYTHONPATH=/code/src
EXPOSE 5000