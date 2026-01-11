FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY x402jobs_api.py .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "x402jobs_api:app", "--host", "0.0.0.0", "--port", "8000"]
