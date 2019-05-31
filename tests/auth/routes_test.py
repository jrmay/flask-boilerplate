from flask_boilerplate.auth.util import do_login


def test_register_page_renders(client):
    response = client.get('/auth/register')
    assert b'Username' in response.data


def test_registering(client):
    username = 'newuser'
    password = 'password'
    data = {'username': username, 'password': password}
    response = client.post('/auth/register', data=data)
    assert response.status_code == 302


def test_registering_without_username_fails(client):
    username = ''
    password = 'password'
    data = {'username': username, 'password': password}
    response = client.post('/auth/register', data=data)
    assert b'Username is required.' in response.data


def test_registering_without_password_fails(client):
    username = 'newuser'
    password = ''
    data = {'username': username, 'password': password}
    response = client.post('/auth/register', data=data)
    assert b'Password is required' in response.data


def test_registering_existing_user_fails(client):
    username = 'jordanmay'
    password = 'password'
    data = {'username': username, 'password': password}
    response = client.post('/auth/register', data=data)
    assert b'User jordanmay is already registered' in response.data


def test_login_page_renders(client):
    response = client.get('/auth/login')
    assert b'Username' in response.data


def test_login_page_shows_log_out_when_authed(client):
    with client:
        username = 'jordanmay'
        password = 'password'
        data = {'username': username, 'password': password}
        _ = client.post('/auth/login', data=data)
        response = client.get('/auth/login')
    assert b'Log out' in response.data


def test_logging_in(client):
    username = 'jordanmay'
    password = 'password'
    data = {'username': username, 'password': password}
    response = client.post('/auth/login', data=data)
    assert response.status_code == 302


def test_logging_in_with_bad_username_fails(client):
    username = 'notauser'
    password = 'password'
    data = {'username': username, 'password': password}
    response = client.post('/auth/login', data=data)
    assert b'Incorrect username' in response.data


def test_logging_in_with_bad_password_fails(client):
    username = 'jordanmay'
    password = 'incorrect'
    data = {'username': username, 'password': password}
    response = client.post('/auth/login', data=data)
    assert b'Incorrect password' in response.data


def test_logout(client):
    with client:
        client.get('/')  # Arbitrary route, need a request context to do_login
        do_login('jordanmay', 'password')
        response = client.get('/auth/logout')
    assert response.status_code == 302
    assert 'session=;' in response.headers['Set-Cookie']
