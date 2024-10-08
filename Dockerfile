FROM python:3.9
RUN apt-get update
RUN apt-get install -y --no-install-recommends postgresql-client unzip vim
RUN apt-get install -y nginx
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

RUN chmod +755 start.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
