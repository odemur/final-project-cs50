from app.models.property import Property
from app import db

def test_property_model(session):
    property = Property(
        title='Test Property',
        description='This is a test property',
        address='123 Test St',
        city='Test City',
        state='Test State',
        price=100000.0
    )
    db.session.add(property)
    db.session.commit()
    assert Property.query.get(property.id) == property
