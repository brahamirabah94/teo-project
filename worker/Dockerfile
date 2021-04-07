FROM python:3
RUN pip install redis
COPY worker.py /
expose 80
CMD ['pyhton', 'worker.py']