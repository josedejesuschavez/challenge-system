FROM python:3.9.1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

WORKDIR /code/src/Infraestructure/Web/Flask

CMD ["python", "wsgi.py"]
EXPOSE 5000