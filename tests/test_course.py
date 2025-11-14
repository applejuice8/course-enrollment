from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Create
def test_create_course():
    payload = {
        'code': 'FEL1847',
        'name': 'Database Fundamentals',
        'credit_hours': 4
    }
    response = client.post('/courses/', json=payload)
    data = response.json()

    assert response.status_code == 200
    for key, value in payload.items():
        assert data[key] == value

    client.delete(f'/courses/{data['id']}')     # Delete after test

# Read
def test_get_courses():
    response = client.get('/courses/')
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    for course in data:
        assert set(course.keys()) == {'id', 'code', 'name', 'credit_hours'}

def test_get_course():
    response = client.get('/courses/1')
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert set(data.keys()) == {'id', 'code', 'name', 'credit_hours'}

# Update


# Delete
