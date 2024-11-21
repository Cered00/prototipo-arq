from flask import Blueprint, request, jsonify
from controllers.DepartamentController import DepartamentController, PaymentController

departament_blueprint = Blueprint('departament_blueprint', __name__)

class DepartamentView:

    @staticmethod
    @departament_blueprint.route('/departament/create', methods=['POST'])
    def create_departament():
        data = request.get_json()
        departament = DepartamentController.create_departament(data)
        return jsonify({"status": True, "departament": departament.serialize()}), 201
    
    @staticmethod
    @departament_blueprint.route('/departament/<int:departament_id>', methods=['GET'])
    def get_departament_by_id(departament_id):
        departament = DepartamentController.get_departament_by_id(departament_id)

        if not departament:
            return jsonify({"status": False, "message": "Departament not found"}), 404

        return jsonify({"status": True, "departament": departament.serialize()}), 200
    
    @staticmethod
    @departament_blueprint.route('/departament/all', methods=['GET'])
    def get_all_departaments():
        departaments = DepartamentController.get_all_departaments()
        return jsonify({"status": True, "departaments": [departament.serialize() for departament in departaments]}), 200
    
class PaymentView:

    @staticmethod
    @departament_blueprint.route('/payment/create', methods=['POST'])
    def create_payment():
        data = request.get_json()
        payment = PaymentController.create_payment(data['resident_id'], data['payment_method'], data['description'], data['confirm_method'], data['amount'])
        return jsonify({"status": True, "payment": payment.serialize()}), 201
    
    @staticmethod
    @departament_blueprint.route('/payment/<int:payment_id>', methods=['GET'])
    def get_payment_by_id(payment_id):
        payment = PaymentController.get_payment_by_id(payment_id)

        if not payment:
            return jsonify({"status": False, "message": "Payment not found"}), 404

        return jsonify({"status": True, "payment": payment.serialize()}), 200
    
    @staticmethod
    @departament_blueprint.route('/payment/all', methods=['GET'])
    def get_all_payments():
        payments = PaymentController.get_all_payments()
        return jsonify({"status": True, "payments": [payment.serialize() for payment in payments]}), 200
    
    @staticmethod
    @departament_blueprint.route('/payment/finish/<int:payment_id>', methods=['PUT'])
    def finish_payment(payment_id):
        payment = PaymentController.finish_payment(payment_id)
        return jsonify({"status": True, "payment": payment.serialize()}), 200