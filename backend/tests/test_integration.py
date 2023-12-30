from app import create_app, db

def test_create_property_integration():
    app = create_app('testing')
    with app.app_context():
        db.create_all()

        client = app.test_client()
        response = client.post('/properties', json={
            'title': 'Test Property',
            'description': 'This is a test property',
            'address': '123 Test St',
            'city': 'Test City',
            'state': 'Test State',
            'price': 100000.0
        })
        assert response.status_code == 201

        data = response.get_json()
        assert 'id' in data
        assert data['title'] == 'Test Property'

        db.drop_all()