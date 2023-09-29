# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the service files into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 9090 for the FastAPI application
EXPOSE 9090

# Run the supervisor script to coordinate the producer, consumer, and FastAPI server
CMD ["python", "supervisor.py"]