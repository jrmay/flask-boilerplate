def test_register_page_renders(client):
    response = client.get('/auth/register')
    assert b'Username' in response.data


def test_registering(client):
    username = 'newuser'
    password = 'password'
    response = client.post('/auth/register', data={'username': username, 'password': password})
    assert response.status_code == 302


def test_registering_without_username_fails(client):
    username = ''
    password = 'password'
    response = client.post('/auth/register', data={'username': username, 'password': password})
    assert b'Username is required.' in response.data


def test_registering_without_password_fails(client):
    username = 'newuser'
    password = ''
    response = client.post('/auth/register', data={'username': username, 'password': password})
    assert b'Password is required' in response.data


def test_registering_existing_user_fails(client):
    username = 'jordanmay'
    password = 'password'
    response = client.post('/auth/register', data={'username': username, 'password': password})
    print(response.data)
    assert b'User jordanmay is already registered' in response.data


def test_login_page_renders(client):
    response = client.get('/auth/login')
    assert b'Username' in response.data


def test_logging_in(client):
    username = 'jordanmay'
    password = 'password'
    response = client.post('/auth/login', data={'username': username, 'password': password})
    assert response.status_code == 302


def test_logging_in_with_bad_username_fails(client):
    username = 'notauser'
    password = 'password'
    response = client.post('/auth/login', data={'username': username, 'password': password})
    assert b'Incorrect username' in response.data


def test_logging_in_with_bad_password_fails(client):
    username = 'jordanmay'
    password = 'incorrect'
    response = client.post('/auth/login', data={'username': username, 'password': password})
    assert b'Incorrect password' in response.data