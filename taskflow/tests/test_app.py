from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    payload = response.get_json()
    assert payload['app'] == 'taskflow'
    assert payload['status'] == 'running'
    assert 'version' in payload
    assert 'environment' in payload


def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')

    assert response.status_code == 200
    payload = response.get_json()
    assert payload['status'] == 'ok'
    assert payload['service'] == 'taskflow'
    assert 'version' in payload
