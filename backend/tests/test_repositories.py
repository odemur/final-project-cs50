from app.repositories.property_repository import PropertyRepository
from app.models.property import Property

def test_create_property(session):
    repository = PropertyRepository()
    property = repository.create_property(
        title='Test Property',
        description='This is a test property',
        address='123 Test St',
        city='Test City',
        state='Test State',
        price=100000.0
    )
    assert Property.query.get(property.id) == property