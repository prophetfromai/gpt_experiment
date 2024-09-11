# -----------------------------------------------------------
# Stage 1: Build a virtual environment with dependencies
# -----------------------------------------------------------

FROM debian:12-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel


# -----------------------------------------------------------
# Stage 2: Install Python dependencies in the virtualenv
# -----------------------------------------------------------

FROM build AS build-venv

COPY requirements.txt /requirements.txt

RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt


# -----------------------------------------------------------
# Stage 3: Create the final production image (Distroless)
# -----------------------------------------------------------

FROM gcr.io/distroless/python3-debian12

COPY --from=build-venv /venv /venv

# Copy the FastAPI application code, templates, and static files to the container
COPY ./app /app
COPY ./app/templates /app/templates 
COPY ./app/static /app/static
COPY start.py ./start.py

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the entry point to start the FastAPI server
ENTRYPOINT ["/venv/bin/python3", "start.py"]
