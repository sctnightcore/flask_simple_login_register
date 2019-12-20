from flask import url_for

def test_router_index(client):
    assert client.get(url_for("router.index")).status_code == 200

def test_router_login(client):
    assert client.get(url_for("router.login")).status_code == 200
    
def test_router_register(client):
    assert client.get(url_for("router.register")).status_code == 200