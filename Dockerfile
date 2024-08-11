# Use an official Python runtime as a parent image

#!/bin/bash

FROM --platform=linux/amd64 python:3-alpine3.19

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install additional dependencies for building certain Python packages
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run main.py when the container launches
CMD ["python", "./main.py"]
