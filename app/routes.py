from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import verify_firebase_token  

# Create a router object that will handle paths prefixed with "/shop"
router = APIRouter(prefix="/shop", tags=["shop"])


# Define data models using Pydantic
class HelloWorldResponse(BaseModel):
    """Model for a hello world response message."""
    message: str


class Item(BaseModel):
    """Model representing an item in the shop with an id and a name."""
    id: int
    name: str


class ItemCreateRequest(BaseModel):
    """Data model for the payload needed to create an item, only needs a name."""
    name: str


class ItemUpdateRequest(BaseModel):
    """Data model for updating an item's name."""
    name: str


# Initialize sample data, simulating a database of items
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]


# Define API endpoints

# Public endpoint (doesn't require authentication)
@router.get("/", response_model=HelloWorldResponse)
def hello_world():
    """
    Returns a simple hello world message.
    """
    return {"message": "Hello, world!"}


# Secured endpoint: only accessible with valid Firebase token
@router.get("/items", response_model=List[Item])
def get_all_items(user_info: dict = Depends(verify_firebase_token)):
    """
    Retrieves all items currently available in the shop.
    Requires authentication.
    """
    return items


# Secured endpoint: creating a new item (requires authentication)
@router.post("/items", response_model=Item)
def create_item(item: ItemCreateRequest, user_info: dict = Depends(verify_firebase_token)):
    """
    Creates a new item in the shop.
    Requires authentication.
    """
    new_item = {"id": len(items) + 1, "name": item.name}
    items.append(new_item)
    return new_item


# Secured endpoint: updating an item (requires authentication)
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdateRequest, user_info: dict = Depends(verify_firebase_token)):
    """
    Updates an existing item by its ID.
    Requires authentication.
    """
    for index, current_item in enumerate(items):
        if current_item["id"] == item_id:
            items[index]["name"] = item.name
            return items[index]
    return {"error": "Item not found"}, 404


# Secured endpoint: deleting an item (requires authentication)
@router.delete("/items/{item_id}", response_model=HelloWorldResponse)
def delete_item(item_id: int, user_info: dict = Depends(verify_firebase_token)):
    """
    Deletes an item by ID from the shop.
    Requires authentication.
    """
    global items  # Necessary for modifying the list within this function
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}
