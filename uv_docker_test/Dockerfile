# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl (required for fetching uv)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Download and run the uv installer using curl, then remove the installer script
RUN curl -fsSL https://astral.sh/uv/install.sh -o /uv-installer.sh && \
    sh /uv-installer.sh && \
    rm /uv-installer.sh

# Ensure the installed binary is on the PATH and set BLIS_ARCH
ENV PATH="/root/.local/bin:$PATH" \
    BLIS_ARCH=generic

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock ./

# Copy source code
COPY main.py ./

# Sync dependencies
RUN uv sync --frozen --no-cache

# Define the default command for the container
CMD ["uv", "run", "main.py"]
