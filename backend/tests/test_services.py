from app.services.property_service import PropertyService
from app.repositories.property_repository import PropertyRepository

def test_create_property_service(session):
    repository = PropertyRepository()
    service = PropertyService(repository)
    property = service.create_property(
        title='Test Property',
        description='This is a test property',
        address='123 Test St',
        city='Test City',
        state='Test State',
        price=100000.0
    )
    assert Property.query.get(property.id) == property