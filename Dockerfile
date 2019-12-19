
FROM python:3.6.1

WORKDIR /eurovision

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python3", "app.py"]


