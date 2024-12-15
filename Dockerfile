# Używamy obrazu Pythona jako bazy
FROM python:3.9-slim

# Instalacja zależności systemowych (np. dla MySQL)
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiowanie pliku z wymaganiami
COPY requirements.txt /app/

# Instalacja zależności Python
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie aplikacji do kontenera
COPY . /app/

# Eksponowanie portu aplikacji
EXPOSE 5050

# Uruchomienie aplikacji
CMD ["python", "api.py"]
