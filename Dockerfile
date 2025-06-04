# Вибираємо базовий образ з Python 3.9 (або 3.10)
FROM python:3.9-slim

# Оновлюємо пакети та встановлюємо системні бібліотеки для збірки
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проекту
COPY . /app

# Створюємо віртуальне оточення в /opt/venv
RUN python3 -m venv /opt/venv

# Оновлюємо pip, setuptools, wheel у віртуальному оточенні
RUN /opt/venv/bin/pip install --upgrade pip setuptools wheel

# Встановлюємо залежності з requirements.txt у віртуальному оточенні
RUN /opt/venv/bin/pip install -r requirements.txt

# Додаємо /opt/venv/bin в PATH, щоб запускати команди з віртуального оточення
ENV PATH="/opt/venv/bin:$PATH"

# Вказуємо команду запуску бота (заміни app.py на твій файл)
CMD ["python", "app.py"]
