FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY . .
# RUN pip install requirements.txt
RUN pip  install -r requirements.txt
ENV FLASK_APP=app.py

# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-w 4", "-b :5000", "app:app"]
