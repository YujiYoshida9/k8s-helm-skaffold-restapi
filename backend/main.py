from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items = [
    Item(id=1, name="Item 1", description="Description for Item 1", price=10.0, tax=1.0),
    Item(id=2, name="Item 2", description="Description for Item 2", price=20.0, tax=2.0),
    Item(id=3, name="Item 3", description="Description for Item 3", price=30.0, tax=3.0),
]

def find_item(item_id: int):
    return next((item for item in items if item.id == item_id), None)

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return items[skip: skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = find_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_index] = updated_item
    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item_index = next((index for index, item in enumerate(items) if item.id == item_id), None)
    if item_index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_index]
    return {"detail": "Item deleted"}
