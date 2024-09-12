FROM python:3.11-slim
LABEL authors="kamal"

ENV PYTHONUNBUFFERED 1

# Create the application build directory
RUN mkdir /sojo-weather-api
WORKDIR /sojo-weather-api

# Install / update core packages
RUN apt-get update && apt-get clean

# Copy project to workdir
COPY ./src ./src

# Copy needed files
COPY settings.py .
COPY requirements.txt .
COPY main.py .


# Install dependencies and expose port of health check
RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 install -r requirements.txt

# Open server port
EXPOSE 8000

# Run main file
CMD python main.py
