# Usa una immagine python leggera
FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file necessari
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Espone la porta
EXPOSE 4000

# Comando per lanciare l'app
CMD ["python", "app.py"]