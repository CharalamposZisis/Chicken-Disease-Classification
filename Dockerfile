FROM python:3.8-slim

# Install system dependencies: git + awscli
RUN apt update -y && \
    apt install -y git awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command
CMD ["python3", "app.py"]
