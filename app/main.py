"""
This module is the main entry point for the FastAPI application.

It initializes the FastAPI app, includes all the route definitions from different routers,
and configures middleware, event handlers, and other application-level configurations.

The application can be started by running this module with a WSGI server like Uvicorn.
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routes import router  # Use relative import
from .config import custom_openapi  # Use relative import

# Initialize FastAPI app
app = FastAPI(
    title="My API",
    version="1.0.0",  # Set your desired version here
)

# Include routes from routes.py
app.include_router(router)

# Set custom OpenAPI
app.openapi = custom_openapi(app)

# Redirect base URL to /docs
@app.get("/", include_in_schema=False)  # include_in_schema=False hides it from the OpenAPI docs
async def redirect_to_docs():
    """
    Redirects the base URL to the API documentation.
    """
    return RedirectResponse(url="/docs")