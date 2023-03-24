FROM --platform=linux/amd64 python:3.7

RUN mkdir /app
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "/app/app.py"]
