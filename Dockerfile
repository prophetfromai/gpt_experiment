# -----------------------------------------------------------
# Stage 1: Build a virtual environment with dependencies
# -----------------------------------------------------------

# Use a minimal Debian base image for building the Python virtual environment.
# The `debian:12-slim` image is lightweight and includes the essentials without unnecessary bloat.
FROM debian:12-slim AS build

# Update the package manager (apt) and install necessary packages:
# - `python3-venv`: Required to create a Python virtual environment.
# - `gcc` and `libpython3-dev`: Necessary to compile C extensions in some Python packages.
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    
    # Create a virtual environment at `/venv` using the installed Python.
    python3 -m venv /venv && \
    
    # Upgrade pip, setuptools, and wheel in the virtual environment to the latest versions.
    # These tools are used to install and build Python packages.
    /venv/bin/pip install --upgrade pip setuptools wheel


# -----------------------------------------------------------
# Stage 2: Install Python dependencies in the virtualenv
# -----------------------------------------------------------

# This is a separate stage to build the virtual environment. The idea is that this step will only be re-executed
# if the `requirements.txt` file changes (thanks to Docker's caching mechanism).
FROM build AS build-venv

# Copy the `requirements.txt` file (which contains the list of Python dependencies) from the local machine
# to the container. This is required to install the specified packages in the virtual environment.
COPY requirements.txt /requirements.txt

# Install the required Python dependencies from `requirements.txt` into the virtual environment using pip.
# The `--disable-pip-version-check` flag avoids unnecessary version checks and speed up the build process.
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt


# -----------------------------------------------------------
# Stage 3: Create the final production image (Distroless)
# -----------------------------------------------------------

# Switch to the final image, using Google’s "distroless" base image.
# The distroless image is extremely minimal (doesn’t even include a shell like bash or sh).
# It includes only what is required to run Python, which improves security and reduces image size.
FROM gcr.io/distroless/python3-debian12

# Copy the virtual environment from the previous `build-venv` stage to the final image.
# The virtual environment contains all the installed Python dependencies.
COPY --from=build-venv /venv /venv

# Copy the FastAPI application code from the local machine to the container.
# The `app` directory contains your FastAPI app, and `start.py` contains the code to start the server.
COPY ./app /app
COPY start.py ./start.py


# -----------------------------------------------------------
# Set important Python environment variables for runtime behavior
# -----------------------------------------------------------

# 1. Prevent Python from writing .pyc (bytecode) files to the filesystem.
#    This helps keep the container lightweight and prevents unnecessary filesystem writes.
ENV PYTHONDONTWRITEBYTECODE=1

# 2. Force Python to immediately flush its output (logs) to the terminal.
#    Without this, Python buffers logs, meaning they may not appear in real-time.
#    This is crucial in containerized environments for debugging and monitoring purposes.
ENV PYTHONUNBUFFERED=1


# -----------------------------------------------------------
# Specify how the container should start the FastAPI app
# -----------------------------------------------------------

# The `ENTRYPOINT` defines the default command that will be run when the container starts.
# Since distroless images don’t include a shell (like bash or sh), we directly call the Python binary in the virtualenv.
# We use the `start.py` file as the entry point, which should handle starting the FastAPI server with Uvicorn.
ENTRYPOINT ["/venv/bin/python3", "start.py"]
