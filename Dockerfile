# Use a slim Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code to the container
COPY ./app ./app

# Expose the application port
EXPOSE 8000

# Run the Uvicorn server directly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
