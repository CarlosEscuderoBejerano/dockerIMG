FROM python:3.9.16-alpine3.16

WORKDIR /carlosflask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 80


ENTRYPOINT [ "/entry_point.sh"]