# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install less for viewing log files and bc for float operations
RUN apt-get update && apt-get install -y less bc

# Make sure the scripts are executable
RUN chmod +x /app/scripts/*.sh

# Make sure results directory is writable, create if does not exist
RUN mkdir -p /app/results && chmod -R u+w /app/results

# Command to run on container start
CMD ["/app/scripts/measure_time.sh"]
