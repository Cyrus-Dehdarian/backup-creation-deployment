# Use the base Python image
FROM docker.io/arm32v7/python:3.9.18-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable
ENV ENV_VAR_NAME=value

# Specify the command to run on container start
CMD ["python", "backend.py"]