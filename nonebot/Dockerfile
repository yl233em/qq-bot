FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "bot.py"]
