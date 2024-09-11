import firebase_admin
from firebase_admin import auth
from fastapi import HTTPException, Header
from typing import Annotated

# Function to verify Firebase token
async def verify_firebase_token(authorization: Annotated[str, Header()]):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    try:
        # Extract the token from "Bearer <token>" format
        id_token = authorization.split("Bearer ")[1]
        
        # Verify the token with Firebase Admin SDK
        decoded_token = auth.verify_id_token(id_token)
        
        return decoded_token

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid token or verification failed: {str(e)}")

# from the browser to get the token
# const token = localStorage.getItem('firebaseToken');
# const authHeader = `Bearer ${token}`;
# console.log('Authorization token for Swagger:', authHeader);
