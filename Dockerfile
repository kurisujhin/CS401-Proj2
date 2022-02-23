FROM python:3.7-slim

WORKDIR ./

COPY predict.py ./
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 
ENV FLASK_APP predict

CMD ["flask","run","--host=0.0.0.0","--port=5018"]