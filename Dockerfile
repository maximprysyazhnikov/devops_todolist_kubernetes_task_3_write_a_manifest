<<<<<<< HEAD
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create migrations and migrate
RUN python manage.py migrate

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
# Використовуємо офіційний образ Python 3.10
FROM python:3.10

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли з репозиторію в контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Прогріваємо міграції бази даних
RUN python manage.py migrate

# Відкриваємо порт 8080
EXPOSE 8000

# Запускаємо сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> ef506944fb06619c48e3d73f3d76ae645e6defd7
