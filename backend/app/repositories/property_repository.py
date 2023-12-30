from app.models.property import db, Property

class PropertyRepository:
    def create_property(self, title, description, address, city, state, price):
        property = Property(title=title, description=description, address=address, city=city, state=state, price=price)
        db.session.add(property)
        db.session.commit()
        return property

    def get_all_properties(self):
        return Property.query.all()

    def get_property_by_id(self, property_id):
        return Property.query.get(property_id)

    def update_property(self, property_id, title, description, address, city, state, price):
        property = Property.query.get(property_id)
        if property:
            property.title = title
            property.description = description
            property.address = address
            property.city = city
            property.state = state
            property.price = price
            db.session.commit()
        return property

    def delete_property(self, property_id):
        property = Property.query.get(property_id)
        if property:
            db.session.delete(property)
            db.session.commit()
        return property