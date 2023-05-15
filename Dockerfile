FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3030

ENV NAME World

CMD ["python","app.py"]

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3030"]