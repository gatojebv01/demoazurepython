# Use a minimal, lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of your local src folder into the container's working directory
COPY src/ /app/

# Expose port 8080 as specified in your script
EXPOSE 8080

# Run the script directly from the container's /app directory
CMD ["python", "app.py"]

