# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Create a virtual environment
RUN pip install virtualenv && virtualenv env

RUN env/bin/python -m pip install --upgrade pip

# Activate the virtual environment and install dependencies
RUN . env/bin/activate && pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=runApp.py

# Run migrations and then run the Flask app
CMD ["bash"]
