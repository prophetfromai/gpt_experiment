from fastapi import FastAPI
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
