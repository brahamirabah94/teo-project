FROM python:3
RUN pip install redis
COPY worker.py /
EXPOSE 80
CMD ["python", "worker.py"]
