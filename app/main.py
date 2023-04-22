from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

GroceryItems = []

class GroceryItem(BaseModel):
    name: str
    quantity: int
    department: str = "uncategorized"

@app.get("/")
async def GetHomepage():
    return {"message": "Welcome :)"}

@app.post("/grocery-items/")
async def CreateItem(item: GroceryItem):
    GroceryItems.append(item)
    return {"item": item}

@app.get("/grocery-items/")
async def GetAllItems():
    return {"items": GroceryItems}

#add delete, edit item, check/uncheck
#create new list, edit, delete, show list
#sort by name, dep