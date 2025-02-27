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
