# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./src/ ./src/
COPY ./data/ ./data/

# Ensure the model directory exists and is copied
RUN mkdir -p model

# Run the training script during the build
RUN python src/train.py

# Expose the port for the API
EXPOSE 8000


# Run the FastAPI app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
