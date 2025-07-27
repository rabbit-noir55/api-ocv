FROM python:3.12-slim

# Zaruriy system kutubxonalarni o‘rnatamiz
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Ishchi katalog
WORKDIR /app

# requirements.txt'ni ko‘chir
COPY requirements.txt .

# PIP orqali kutubxonalarni o‘rnat
RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani nusxa ol
COPY . .

# Gunicorn orqali appni ishga tushirish
CMD exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT}
