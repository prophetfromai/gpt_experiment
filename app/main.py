from fastapi import FastAPI
from .routes import router  # Use relative import
from .config import custom_openapi  # Use relative import
import uvicorn
import os

# Initialize FastAPI app
app = FastAPI()

# Include routes from routes.py
app.include_router(router)

# Set custom OpenAPI
app.openapi = custom_openapi(app)

if __name__ == "__main__":
    # Run the Uvicorn server to serve the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
