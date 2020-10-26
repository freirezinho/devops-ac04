FROM python:3.6.1-alpine
RUN pip install flask
COPY /app/app.py /app.py
CMD ["python", "app.py"]