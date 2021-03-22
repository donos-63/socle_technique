from flask import url_for

def test_hello_world(client, admin_headers):
    # test 200
    resp = client.post("/example/hello_world", headers=admin_headers)
    assert resp.status_code == 200
    
    data = resp.get_json()["message"]
    assert data == "Hello world!"