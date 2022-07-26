from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

ITEMS = [
  {
    "name": "carkey",
    "id": 1
  },
  {
    "name": "shoe",
    "id": 2
  },
  {
    "name": "wallet",
    "id": 3
  },
  {
    "name": "phone",
    "id": 4
  },
  {
    "name": "knife",
    "id": 5
  }
]

class Item(BaseModel):
  name: str
  id: int

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/item")
def read_items():
  return jsonable_encoder(ITEMS);

@app.get("/item/{item_id}")
def read_item_by_id(item_id: int):
  for item in ITEMS:
    if item.get("id") == int(item_id):
      return item

@app.post("/item/")
def add_item(item: Item):
  print(item);
  ITEMS.append(item);
  return { "POST": f"Added {item} to the list of ITEMS" }

@app.put("/item/{item_id}")
def update_item(item_id, item: Item):
  for i in ITEMS:
    if i.get("id") == int(item_id):
      i["name"] = item["name"]

  return { "PUT": f"Item {item_id} has been updated to {item}" }

@app.delete("/item/{item_id}")
def remove_item(item_id):
  for item in ITEMS:
    if item.get("id") == item_id:
      ITEMS.pop(item)

  return { "DELETE": f"Item {item_id} has been deleted" }