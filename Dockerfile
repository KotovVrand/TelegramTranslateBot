FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install --upgrade pip setuptools wheel
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

COPY . .

CMD ["/opt/venv/bin/python", "translate_bot.py"]
