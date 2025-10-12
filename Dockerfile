FROM python:3.8-slim

# Install system dependencies: git + build tools + awscli
RUN apt update -y && \
    apt install -y git build-essential libssl-dev libffi-dev python3-dev awscli && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Default command
CMD ["python3", "app.py"]
