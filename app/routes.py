"""
This module defines API routes for the 'shop' service.

It includes endpoints for:
- Retrieving a hello world message
- Retrieving all items
- Creating a new item
- Updating an existing item
- Deleting an item

Pydantic models are used for data validation and serialization.
"""

from typing import List
from fastapi import APIRouter, Request
from pydantic import BaseModel

# Create a router instance with a prefix and tags for grouping
router = APIRouter(prefix="/shop", tags=["shop"])

# Pydantic models


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


@router.get("/", response_model=HelloWorldResponse)
def hello_world():
    """
    Endpoint to return a simple hello world message.
    """
    return {"message": "OK"}


@router.get("/items", response_model=List[dict])
def get_items(request: Request):
    """
    Endpoint to get a list of all items, along with request information.
    """
    
    # Extracting headers
    headers = dict(request.headers)
    
    # Extracting query parameters
    query_params = dict(request.query_params)
    
    # Extracting method
    method = request.method
    
    # Extracting client's IP address (best effort via 'client' tuple)
    client_host = request.client.host if request.client else "Unknown"
    
    # Extracting cookies
    cookies = request.cookies
    
    # Extracting URL path
    url_path = request.url.path
    
    # Extracting full URL
    full_url = str(request.url)
    
    # Extracting scheme (HTTP or HTTPS)
    scheme = request.url.scheme
    
    # Extracting the HTTP version
    http_version = request.scope["http_version"]
    
    # Request scope information (ASGI scope)
    scope = request.scope
    
    # Return all the collected information
    return {
        "message": "Request details",
        "headers": headers,
        "query_params": query_params,
        "method": method,
        "client_ip": client_host,
        "cookies": cookies,
        "url_path": url_path,
        "full_url": full_url,
        "scheme": scheme,
        "http_version": http_version,
        "scope": scope,
        "items": items,
    }



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
