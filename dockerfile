# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Copy the .env file
COPY .env /app/.env

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
