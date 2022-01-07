FROM alpine:latest

RUN apk update
RUN apk add py-pip
RUN apk add --no-cache python3-dev
RUN apk add --no-cache gcc
RUN apk add --no-cache libc-dev
RUN apk add --no-cache g++
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]