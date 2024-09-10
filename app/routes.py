"""
This module defines API routes for a 'shop' service within a web application.

It includes endpoints for various operations:
- Retrieving a simple hello world message.
- Retrieving all items in the shop.
- Creating a new item.
- Updating an existing item.
- Deleting an item.

We use Pydantic models for data validation and serialization, which helps in ensuring the data passed to and from the API matches our expectations.
"""

# Import necessary libraries and classes
from typing import List
from fastapi import APIRouter  # APIRouter is used to manage different routes
from pydantic import BaseModel  # BaseModel is from Pydantic, used to define data models

# Create a router object that will handle paths prefixed with "/shop"
router = APIRouter(prefix="/shop", tags=["shop"])

# Define data models using Pydantic
class HelloWorldResponse(BaseModel):
    """Model for a hello world response message."""
    message: str  # Field for the message

class Item(BaseModel):
    """Model representing an item in the shop with an id and a name."""
    id: int  # Unique identifier for the item
    name: str  # Name of the item

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
@router.get("/", response_model=HelloWorldResponse)
def hello_world():
    """
    Returns a simple hello world message. This is a basic endpoint to demonstrate an API response.
    """
    return {"message": "Hello, world!"}

@router.get("/items", response_model=List[Item])
def get_all_items():
    """
    Retrieves all items currently available in the shop. This demonstrates how to return a list of items.
    """
    return items  # Returns the list of items

@router.post("/items", response_model=Item)
def create_item(item: ItemCreateRequest):
    """
    Creates a new item in the shop with the provided name. Demonstrates handling POST requests and data creation.
    """
    new_item = {"id": len(items) + 1, "name": item.name}
    items.append(new_item)
    return new_item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdateRequest):
    """
    Updates an existing item by its ID with a new name. Demonstrates handling PUT requests and data updating.
    """
    for index, current_item in enumerate(items):
        if current_item["id"] == item_id:
            items[index]["name"] = item.name
            return items[index]
    return {"error": "Item not found"}, 404

@router.delete("/items/{item_id}", response_model=HelloWorldResponse)
def delete_item(item_id: int):
    """
    Deletes an item by ID from the shop. Demonstrates how to handle DELETE requests and remove data.
    """
    global items  # Necessary for modifying the list within this function
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}

