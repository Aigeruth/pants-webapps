from flask import url_for


def test_app(client):
    response = client.get(url_for('healthcheck'))
    assert response.status_code == 200
    assert response.json == {'status': 'green'}
