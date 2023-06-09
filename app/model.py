from pydantic import BaseModel

class GroceryItem(BaseModel):
    name: str
    quantity: int
    department: str = "uncategorized"