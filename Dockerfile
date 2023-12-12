FROM python:3.10
WORKDIR /app
COPY /templates /app/templates
COPY app.py /app
COPY Dockerfile /app
COPY requirements.txt /app
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV NAME webapp
CMD ["python", "app.py"]


