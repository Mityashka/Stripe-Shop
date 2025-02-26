FROM python:3.10

WORKDIR /shop

COPY requirements.txt /shop/
RUN pip install -r requirements.txt

COPY . /shop/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
