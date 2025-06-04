FROM python:3.9-slim

WORKDIR /app

RUN python -m venv /opt/venv

# Оновлюємо pip, setuptools, wheel
RUN /opt/venv/bin/pip install --upgrade pip setuptools wheel

# Копіюємо всі файли проекту
COPY . .

# Встановлюємо залежності
RUN /opt/venv/bin/pip install -r requirements.txt

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "translate_bot.py"]
