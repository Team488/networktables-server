FROM python:3-alpine

RUN pip install pynetworktables

EXPOSE 1735

COPY server.py .

CMD ["python", "server.py"]