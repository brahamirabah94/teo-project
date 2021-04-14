FROM python:3
RUN pip install redis && \
    pip install requests
COPY worker.py /
EXPOSE 80
CMD ["python", "worker.py"]
