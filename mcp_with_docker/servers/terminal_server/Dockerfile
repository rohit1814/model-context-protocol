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

# Ensure the installed binary is on the PATH and set BLIS_ARCH to use a generic build configuration
ENV PATH="/root/.local/bin:$PATH" \
    BLIS_ARCH=generic

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies 
RUN uv sync --frozen --no-cache

# Now copy the rest of the application
COPY . /app

# Expose the desired port
# EXPOSE 5000

# Run the server using uv
CMD [ "uv", "run", "terminal_server.py" ]

