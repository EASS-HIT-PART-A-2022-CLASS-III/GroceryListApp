from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def testAll():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome :)"}
    response = client.post("/grocery-items/",json={"name":"Milk","quantity":1,"department":"Dairy"})
    assert response.status_code == 200
    assert response.json() == {"message":"added Milk x1 from Dairy to your list"}
    response = client.get("/grocery-items/")
    assert response.status_code == 200
    assert response.json() == {"Dairy":{"Milk":1}}
    response = client.put("/grocery-items/",json={"name":"Milk","quantity":2,"department":"Dairy"})
    assert response.status_code == 200
    assert response.json() == {'message': "Updated name='Milk' quantity=2 department='Dairy' from your list"}
    response = client.delete("/grocery-items/Milk")
    assert response.status_code == 200
    assert response.json() == {"message":"deleted Milk from your list"}