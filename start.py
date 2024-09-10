"""
This module is responsible for starting the FastAPI application using Uvicorn.

It reads environment variables (e.g., PORT) to configure the Uvicorn server dynamically,
ensuring the application runs with the correct settings in different environments.

To start the FastAPI application, run this module as the main entry point.
"""

# Import necessary modules from the standard library and third-party packages.
import os  # Used to interact with the operating system, especially for reading environment variables.
import uvicorn  # Uvicorn is imported to serve as the ASGI server that will run the FastAPI application.

# This conditional check ensures that this script runs only if it is executed as the main program.
if __name__ == "__main__":
    # Get the port number from the environment variables. 
    # This allows for flexibility in deployments across different environments.
    # The default port 8080 is used if no PORT environment variable is set.
    port = int(os.getenv("PORT", "8080"))

    # This function call starts the Uvicorn server with specified configuration.
    # "app.main:app" tells Uvicorn where to find the FastAPI "app" instance in the project structure:
    # - "app.main" is the Python module (main.py inside the app folder).
    # - "app" is the FastAPI instance created and initialized in that module.
    # The host "0.0.0.0" makes the server accessible externally, not just locally.
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
