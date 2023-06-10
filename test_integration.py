import requests as rq
import httpx

def testAll():
    response = rq.get("http://localhost:8000/")
    assert response.status_code == 200
    response = rq.post("http://localhost:8000/v2/grocery-items/",json={"name":"NameTest","quantity":100,"department":"DepTest"})
    assert response.status_code == 200
    response = rq.get("http://localhost:8000/v2/grocery-items/")
    assert response.status_code == 200
    response = rq.put("http://localhost:8000/v2/grocery-items/",json={"name":"NameTest","quantity":200,"department":"DepTest"})
    assert response.status_code == 200
    response = rq.delete(f"http://localhost:8000/v2/grocery-items/NameTest")
    assert response.status_code == 200