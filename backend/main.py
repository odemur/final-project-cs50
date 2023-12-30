from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config
from app.models.property import db
from app.services.property_service import PropertyService

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    CORS(app)

    @app.route('/properties', methods=['POST'])
    def create_property():
        data = request.get_json()
        property_service = PropertyService()
        property = property_service.create_property(
            title=data['title'],
            description=data['description'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            price=data['price']
        )
        return jsonify({'id': property.id}), 201

    @app.route('/properties', methods=['GET'])
    def get_all_properties():
        property_service = PropertyService()
        properties = property_service.get_all_properties()
        return jsonify([{
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'address': property.address,
            'city': property.city,
            'state': property.state,
            'price': property.price
        } for property in properties])

    @app.route('/properties/<int:property_id>', methods=['GET'])
    def get_property(property_id):
        property_service = PropertyService()
        property = property_service.get_property_by_id(property_id)
        if property:
            return jsonify({
                'id': property.id,
                'title': property.title,
                'description': property.description,
                'address': property.address,
                'city': property.city,
                'state': property.state,
                'price': property.price
            })
        else:
            return jsonify({'error': 'Property not found'}), 404

    @app.route('/properties/<int:property_id>', methods=['PUT'])
    def update_property(property_id):
        data = request.get_json()
        property_service = PropertyService()
        property = property_service.update_property(
            property_id=property_id,
            title=data['title'],
            description=data['description'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            price=data['price']
        )
        if property:
            return jsonify({
                'id': property.id,
                'title': property.title,
                'description': property.description,
                'address': property.address,
                'city': property.city,
                'state': property.state,
                'price': property.price
            })
        else:
            return jsonify({'error': 'Property not found'}), 404

    @app.route('/properties/<int:property_id>', methods=['DELETE'])
    def delete_property(property_id):
        property_service = PropertyService()
        property = property_service.delete_property(property_id)
        if property:
            return jsonify({'message': 'Property deleted successfully'})
        else:
            return jsonify({'error': 'Property not found'}), 404

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run()
