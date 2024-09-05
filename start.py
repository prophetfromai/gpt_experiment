"""
This module is responsible for starting the FastAPI application using Uvicorn.

It reads environment variables (e.g., PORT) to configure the Uvicorn server dynamically,
ensuring the application runs with the correct settings in different environments.

To start the FastAPI application, run this module as the main entry point.
"""

import os
import uvicorn

if __name__ == "__main__":
    # Get the port from the environment variable, defaulting to 8080 if not set
    port = int(os.getenv("PORT", "8080"))

    # Run Uvicorn programmatically
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
