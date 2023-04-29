
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def testGetHomepage():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome :)"}

def testCreateItem():
    response = client.post("/grocery-items/",json={"name":"Milk","quantity":1,"department":"Dairy"})
    assert response.status_code == 200
    assert response.json() == {"message":"added Milk x1 from Dairy to your list"}

def testGetAllItems():
    response = client.get("/grocery-items/")
    assert response.status_code == 200
    assert response.json() == {"Dairy":{"Milk":1}}

def testEditItem():
    response = client.put("/grocery-items/",json={"name":"Milk","quantity":2,"department":"Dairy"})
    assert response.status_code == 200
    assert response.json() == {'message': "Updated name='Milk' quantity=2 department='Dairy' from your list"}

def testDeleteItem():
    response = client.delete("/grocery-items/Milk")
    assert response.status_code == 200
    assert response.json() == {"message":"deleted Milk from your list"}