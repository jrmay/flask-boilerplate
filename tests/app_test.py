def test_hello_endpoint_says_hello(client):
    response = client.get('/')
    assert b'Hello World!' in response.data


def test_about_endpoint_has_about_title(client):
    response = client.get('/about')
    assert b'<h1>About</h1>' in response.data
