# start.py
import os
import uvicorn

if __name__ == "__main__":
    # Get the port from the environment variable, defaulting to 8080 if not set
    port = int(os.getenv("PORT", 8080))
    
    # Run Uvicorn programmatically
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
