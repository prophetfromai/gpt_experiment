from typing import Generator
from google.cloud import firestore

def get_firestore_client() -> Generator[firestore.Client, None, None]:
    # Initialize the Firestore client
    client = firestore.Client()

    try:
        # Yield the client to be used by the route
        yield client
    finally:
        # No cleanup needed for Firestore client, but this is where you'd handle cleanup if necessary
        pass


# Example Request to Add Data:
# When a user sends a request to add data, the Firebase ID token will be passed in the Authorization header.
# The FastAPI function will use the uid from the decoded token to store the data in a document that is unique to the user.
# Firestore Security Rules:
# As mentioned earlier, to ensure users can only access their own data, you should define Firestore security rules like this:

# service cloud.firestore {
#   match /databases/{database}/documents {
#     match /users/{userId} {
#       allow read, write: if request.auth != null && request.auth.uid == userId;
#     }
#   }
# }
