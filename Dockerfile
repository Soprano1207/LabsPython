FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["python", "lab1/myproject/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "lab2/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "lab3/manage.py", "runserver", "0.0.0.0:8000"]

CMD ["python", "lab1/myproject/manage.py", "runserver", "0.0.0.0:8000"]
