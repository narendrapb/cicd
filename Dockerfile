FROM python:3.10
WORKDIR /app
COPY /templates /app/templates
COPY app.py /app
COPY Dockerfile /app
RUN pip install Flask
EXPOSE 5000
ENV NAME webapp
CMD ["python", "app.py"]

