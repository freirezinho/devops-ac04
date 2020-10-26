FROM python:3.6.1-alpine
RUN source ./bin/activate
RUN pip install -r requirements.txt
COPY /app/app.py /app.py
CMD ["python", "app.py"]