FROM python:3.11-full

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]