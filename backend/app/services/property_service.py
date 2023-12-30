from app.repositories.property_repository import PropertyRepository

class PropertyService:
    def __init__(self, property_repository=None):
        self.property_repository = property_repository or PropertyRepository()

    def create_property(self, title, description, address, city, state, price):
        return self.property_repository.create_property(title, description, address, city, state, price)

    def get_all_properties(self):
        return self.property_repository.get_all_properties()

    def get_property_by_id(self, property_id):
        return self.property_repository.get_property_by_id(property_id)

    def update_property(self, property_id, title, description, address, city, state, price):
        return self.property_repository.update_property(property_id, title, description, address, city, state, price)

    def delete_property(self, property_id):
        return self.property_repository.delete_property(property_id)