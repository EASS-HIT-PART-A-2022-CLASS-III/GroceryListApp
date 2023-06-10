
from fastapi.testclient import TestClient
from main import app
import requests as rq
import httpx

client = TestClient(app)

def testGetHomepage():
    response = client.get("/")
    assert response.status_code == 200

def testCreateItem():
    response = rq.post("http://localhost:8000/v2/grocery-items/",json={"name":"NameTest","quantity":100,"department":"DepTest"})
    assert response.status_code == 200

def testGetAllItems():
    response = rq.get("http://localhost:8000/v2/grocery-items/")
    assert response.status_code == 200

def testEditItem():
    response = rq.put("http://localhost:8000/v2/grocery-items/",json={"name":"NameTest","quantity":200,"department":"DepTest"})
    assert response.status_code == 200

def testDeleteItem():
    response = rq.delete(f"http://localhost:8000/v2/grocery-items/NameTest")
    assert response.status_code == 200
