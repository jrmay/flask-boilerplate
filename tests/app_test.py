def test_hello_endpoint_says_hello(client):
    response = client.get('/')
    assert b'Hello World!' in response.data
