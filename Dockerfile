FROM debian

COPY ./requirements.txt .

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN pip3 install -r requirements.txt

COPY . .

CMD python3 main.py
