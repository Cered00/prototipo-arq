from flask import Blueprint, request, jsonify
from controllers.UserController import ResidentController

user_blueprint = Blueprint('user_blueprint', __name__)

class ResidentView:

    @staticmethod
    @user_blueprint.route('/resident/create', methods=['POST'])
    def create_resident():
        try:
            data = request.get_json()
            resident = ResidentController.create_resident_controller(data)
            return jsonify({"status": True, "resident": resident.serialize()}), 201
        except Exception as e:
            print(e)
            return jsonify({"status": False, "message": "error al crear el usuario"})
    
    
    @staticmethod
    @user_blueprint.route('/resident/<int:resident_id>', methods=['GET'])
    def get_resident_by_id(resident_id):
        resident = ResidentController.get_resident_by_id_controller(resident_id)

        if not resident:
            return jsonify({"status": False, "message": "Resident not found"}), 404

        return jsonify({"status": True, "resident": resident.serialize()}), 200
    
    @staticmethod
    @user_blueprint.route('/resident/all', methods=['GET'])
    def get_all_residents():
        residents = ResidentController.get_all_residents_controller()
        return jsonify({"status": True, "residents": [resident.serialize() for resident in residents]}), 200