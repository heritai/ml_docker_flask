# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /qdock

COPY requirements.txt requirements.txt
COPY paq-0.1.tar.gz paq-0.1.tar.gz

RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flsk", "run", "--host=0.0.0.0"]


# docker build -t qdock . 
# docker run -p 80:5000 qdock 
# docker stop qdock   
