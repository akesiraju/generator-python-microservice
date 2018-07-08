# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /opt
WORKDIR /opt/<%= APP_NAME %>

# Copy the current directory contents into the container at /opt
ADD . /opt/<%= APP_NAME %>

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE <%= PORT %>

# Run app.py when the container launches
CMD ["python", "app.py"]