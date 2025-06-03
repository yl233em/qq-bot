FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml requirements.txt /app/
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app

CMD ["python", "bot.py"]
