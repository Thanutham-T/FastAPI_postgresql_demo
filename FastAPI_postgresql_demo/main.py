from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI PostgreSQL Demo",
              description="A simple FastAPI application demonstrating CRUD operations with PostgreSQL.",
              version="1.0.0")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}


@app.get("/items/{item_id}",
        tags=["items"],
        summary="Read an item",
        description="Get an item by its ID. Optionally, you can provide a query parameter")
def read_item(item_id: int, q: Union[str, None] = None) -> dict:
    return {"item_id": item_id, "q": q}

@app.post("/items/"
          ,tags=["items"],
          summary="Create an item",
          description="Create a new item with a name, price, and optional offer status.")
def create_item(item: Item) -> Item:
    return item

@app.put("/items/{item_id}",
          tags=["items"],
          summary="Update an item",
          description="Update an existing item by its ID. Provide the new item details.")
def update_item(item_id: int, item: Item) -> dict:
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}",
            tags=["items"],
            summary="Delete an item",
            description="Delete an item by its ID.")
async def delete_item(item_id: int) -> dict:
    return {"message": f"Item with id {item_id} deleted successfully."}