from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# Create a router instance
router = APIRouter()

# Pydantic models
class HelloWorldResponse(BaseModel):
    message: str

class Item(BaseModel):
    id: int
    name: str

class ItemCreateRequest(BaseModel):
    name: str

class ItemUpdateRequest(BaseModel):
    name: str

# Sample data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

# Define routes
@router.get("/", response_model=HelloWorldResponse)
def hello_world():
    return {"message": "OK"}

@router.get("/items", response_model=List[Item])
def get_items():
    return items

@router.post("/items", response_model=Item)
def create_item(item: ItemCreateRequest):
    new_item = {"id": len(items) + 1, "name": item.name}
    items.append(new_item)
    return new_item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdateRequest):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            items[i]["name"] = item.name
            return items[i]
    return {"error": "Item not found"}, 404

@router.delete("/items/{item_id}", response_model=HelloWorldResponse)
def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}
