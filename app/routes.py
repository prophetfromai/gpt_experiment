"""
This module defines API routes for the 'shop' service.

Pydantic models are used for data validation and serialization.
"""

from fastapi import APIRouter
from pydantic import BaseModel

# Create a router instance with a prefix and tags for grouping
router = APIRouter(prefix="/shop", tags=["shop"])

class HelloWorldResponse(BaseModel):
    """Model for a hello world response message."""
    message: str


class Item(BaseModel):
    """Model for an item with id and name."""
    id: int
    name: str


class ItemCreateRequest(BaseModel):
    """Model for item creation request with a name."""
    name: str


class ItemUpdateRequest(BaseModel):
    """Model for item update request with a name."""
    name: str


# Sample data
items = [
    {
        "id": 1,
        "name": "Item 1"
    },
    {
        "id": 2,
        "name": "Item 2"
    },
]

# Define routes


@router.get("/items")
def get_item():
    """
    Endpoint to create a new item.
    """

    return items

@router.post("/items", response_model=Item)
def create_item(item: ItemCreateRequest):
    """
    Endpoint to create a new item.
    """
    new_item = {"id": len(items) + 1, "name": item.name}
    items.append(new_item)
    return new_item


@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdateRequest):
    """
    Endpoint to update an existing item by ID.
    """
    for index, current_item in enumerate(items):
        if current_item["id"] == item_id:
            items[index]["name"] = item.name
            return items[index]
    return {"error": "Item not found"}, 404


@router.delete("/items/{item_id}", response_model=HelloWorldResponse)
def delete_item(item_id: int):
    """
    Endpoint to delete an item by ID.
    """
    global items  # pylint: disable=global-statement
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}


@router.get("/testdemo")
def get_item():
    """
    Endpoint to create a new item.
    """

    return 'this happened automatically woop'