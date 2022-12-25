FROM python:latest
WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app/app.py app.py
CMD ["python", "-u", "app.py"]