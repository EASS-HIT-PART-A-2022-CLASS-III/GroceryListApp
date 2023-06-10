import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://root:root@db:27017"
)

db = client.GroceryDB

colletion = db.GroceryCollection

async def DBCreateItem(item: dict):
    out = await colletion.insert_one(item)
    if out:
        return {"message": f'Added {item["name"]} x{item["quantity"]} from {item["department"]} to your list'}
    else:
        return {"Error": "Adding Grocery item failed :("}

async def DBGetAllItems():
    out = {}
    lst = colletion.find()
    async for item in lst:
        if item["department"] not in out:
            out[item["department"]] = {item["name"]:item["quantity"]}
        else:
            out[item["department"]].update({item["name"]:item["quantity"]})
    return out
 

async def DBEditItem(updated: dict):
    out = await colletion.update_one({"name":updated['name']},{"$set":{"quantity":updated['quantity'],"department":updated['department']}})
    if out:
        return{"message":f'Updated {updated["name"]} from your list'}
    else:
        return{"message":f"{updated['name']} not found"}

async def DBDeleteItem(ItemName:str):
    out = await colletion.delete_one({"name":ItemName})
    if out:
        return{"message":f"Removed {ItemName} from your list"}
    else:
        return{"message":f"{ItemName} not found"} 


