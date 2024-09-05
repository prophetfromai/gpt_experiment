"""
This module contains configuration settings for the FastAPI application.

It includes functions and variables that modify the default behavior of the OpenAPI
documentation or any other custom configurations for the application.
"""

import os


def custom_openapi(app):
    """
    Returns a custom OpenAPI schema generation function for the provided FastAPI app.
    """

    # Store the original OpenAPI method
    original_openapi = app.openapi

    def openapi():
        if app.openapi_schema:
            return app.openapi_schema

        # Generate the default OpenAPI schema using the original method
        openapi_schema = original_openapi().copy()

        # Retrieve the server URL from the environment variable
        server_url = os.getenv(
            "BASE_URL",
            "http://localhost:8080")  # Default to local URL if not set

        openapi_schema["servers"] = [{
            "url":
            server_url,
            "description":
            "Production server" if "run.app" in server_url else "Local server"
        }]

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return openapi
