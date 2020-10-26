FROM python:3.6.1-alpine
RUN pip install -r requirements.txt
COPY /app/app.py /app.py
CMD ["python", "app.py"]