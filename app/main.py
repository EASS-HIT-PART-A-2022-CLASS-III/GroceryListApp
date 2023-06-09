from fastapi import FastAPI
from model import GroceryItem 
from database import (DBGetAllItems, DBCreateItem, DBEditItem, DBDeleteItem)

app = FastAPI()

GroceryItems = []

@app.get("/")
async def GetHomepage():
    return {"message": "Welcome :)"}

@app.post("/v1/grocery-items/")
async def CreateItem(item: GroceryItem):
    GroceryItems.append(item)
    return {"message": f"added {item.name} x{item.quantity} from {item.department} to your list"}

@app.post("/v2/grocery-items/")
async def CreateItem(item: GroceryItem):
    msg = await DBCreateItem(item.dict())
    return msg


@app.get("/v1/grocery-items/")
async def GetAllItems():
    out = {}
    for item in GroceryItems:
        if item.department not in out:
            out[item.department] = {item.name:item.quantity}
        else:
            out[item.department].update({item.name:item.quantity})
    return out

@app.get("/v2/grocery-items/")
async def GetAllItems():
    msg = await DBGetAllItems()
    return msg

@app.put("/v1/grocery-items/")
async def EditItem(updated: GroceryItem):
    for item in GroceryItems:
        if item.name == updated.name:
            item.name = updated.name
            item.quantity = updated.quantity
            item.department = updated.department
            return{"message":f"Updated {updated} from your list"}
    return{"message":f"{updated} not found"}

@app.put("/v2/grocery-items/")
async def EditItem(updated: GroceryItem):
    msg = await DBEditItem(updated.dict())
    return msg

@app.delete("/v1/grocery-items/{ItemName}")
async def DeleteItem(ItemName:str):
    for item in GroceryItems:
        if item.name == ItemName:
            GroceryItems.remove(item)
            return{"message":f"deleted {ItemName} from your list"}
    return{"message":f"{ItemName} not found"}  

@app.delete("/v2/grocery-items/{ItemName}")
async def DeleteItem(ItemName:str):
    msg = await DBDeleteItem(ItemName.dict())
    return msg