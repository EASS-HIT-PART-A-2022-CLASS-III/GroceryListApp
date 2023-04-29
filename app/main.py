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
    return {"message": f"added {item.name} x{item.quantity} from {item.department} to your list"}

@app.get("/grocery-items/")
async def GetAllItems():
    out = {}
    for item in GroceryItems:
        if item.department not in out:
            out[item.department] = {item.name:item.quantity}
        else:
            out[item.department].update({item.name:item.quantity})
    return out

@app.put("/grocery-items/")
async def EditItem(updated: GroceryItem):
    for item in GroceryItems:
        if item.name == updated.name:
            item.name = updated.name
            item.quantity = updated.quantity
            item.department = updated.department
            return{"message":f"Updated {updated} from your list"}
    return{"message":f"{updated} not found"}

@app.delete("/grocery-items/{ItemName}")
async def DeleteItem(ItemName:str):
    for item in GroceryItems:
        if item.name == ItemName:
            GroceryItems.remove(item)
            return{"message":f"deleted {ItemName} from your list"}
    return{"message":f"{ItemName} not found"}

#homepage = show list and 3 buttons
#list sorted by name or deparment    