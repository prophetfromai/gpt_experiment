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

from typing import List, Dict, Any, Union
from fastapi import APIRouter, Request, FastAPI
from pydantic import BaseModel
import types

# Create a router instance with a prefix and tags for grouping
router = APIRouter(prefix="/shop", tags=["shop"])


# Define the Pydantic model
class RequestDetails(BaseModel):
    message: str
    headers: Dict[str, str]
    query_params: Dict[str, str]
    method: str
    client_ip: str
    cookies: Dict[str, str]
    url_path: str
    full_url: str
    scheme: str
    http_version: str
    scope: Dict[str, Any]  # Scope may contain complex data, we'll filter this
    items: List[Dict[str,
                     Union[str,
                           int]]]  # Adjust for items that could be int or str


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


# Define the FastAPI route to return this response
@router.get("/request-details", response_model=RequestDetails)
async def get_request_details(request: Request):
    headers = {k: v for k, v in request.headers.items()}
    query_params = dict(request.query_params)
    method = request.method
    client_ip = request.client.host
    cookies = request.cookies
    url_path = request.url.path
    full_url = str(request.url)
    scheme = request.url.scheme
    http_version = request.scope.get("http_version")

    # Filter out non-serializable objects like FastAPI instances, APIRouter, and function types
    scope = {
        key:
        str(value) if isinstance(value,
                                 (tuple, dict, list, str, int)) else None
        for key, value in request.scope.items()
        if not isinstance(value, (FastAPI, APIRouter, type, types.FunctionType
                                  ))  # Exclude functions and internal objects
    }

    # Items example
    items = [{"id": 1}, {"id": 2}]  # Replace with actual items logic

    return RequestDetails(message="Request details",
                          headers=headers,
                          query_params=query_params,
                          method=method,
                          client_ip=client_ip,
                          cookies=cookies,
                          url_path=url_path,
                          full_url=full_url,
                          scheme=scheme,
                          http_version=http_version,
                          scope=scope,
                          items=items)


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
