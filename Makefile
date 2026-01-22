.PHONY: build up down logs shell analyze download clean

# Docker Image Name (optional use if needed, but composed is used)
SERVICE_NAME = gdelt-downloader

# Build the docker image
build:
	docker-compose build

# Start the scheduler in background
up:
	docker-compose up -d

# Stop the scheduler
down:
	docker-compose down

# View logs
logs:
	docker-compose logs -f

# Run a shell inside the container
shell:
	docker-compose run --rm $(SERVICE_NAME) /bin/bash

# Run the analysis script
analyze:
	docker-compose run --rm $(SERVICE_NAME) python src/analyze_sample.py

# Run the downloader explicitly (one-off)
download:
	docker-compose run --rm $(SERVICE_NAME) python src/gdelt_downloader.py

# Clean up pycache and temp files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
