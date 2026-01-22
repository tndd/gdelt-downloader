FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY gdelt_downloader.py .
COPY scheduler.py .
COPY run_daily.sh . 
# Note: run_daily.sh might not be needed inside Docker if we use scheduler.py explicitly

# Create data directory
RUN mkdir -p data/events data/mentions data/gkg

# Default command runs the scheduler
CMD ["python", "scheduler.py"]
