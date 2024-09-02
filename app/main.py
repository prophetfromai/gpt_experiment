from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Define a Pydantic model for the response
class HelloWorldResponse(BaseModel):
    message: str

@app.get("/", response_model=HelloWorldResponse)
def hello_world():
    return {"message": "OK"}

# Store the original OpenAPI method
original_openapi = app.openapi

# Custom OpenAPI schema generation
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = original_openapi().copy()  # Use the stored original method

    # Retrieve the server URL from the environment variable
    server_url = os.getenv("BASE_URL", "http://localhost:8000")  # Default to local URL if not set

    openapi_schema["servers"] = [
        {
            "url": server_url,
            "description": "Production server" if "run.app" in server_url else "Local server"
        }
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Override the default OpenAPI method with the custom one
app.openapi = custom_openapi

if __name__ == "__main__":
    # Run the Uvicorn server to serve the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
