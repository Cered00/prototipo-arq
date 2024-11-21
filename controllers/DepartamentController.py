from services.DepartamentService import DepartamentService, PaymentService

class DepartamentController:
    
        @staticmethod
        def create_departament(data):
            return DepartamentService.create_departament(data)
    
        @staticmethod
        def get_departament_by_id(departament_id):
            return DepartamentService.get_departament_by_id(departament_id)
    
        @staticmethod
        def get_all_departaments():
            return DepartamentService.get_all_departaments()
        
class PaymentController:
        
        @staticmethod
        def create_payment(resident_id, payment_method, description, confirm_method, amount):
            return PaymentService.create_payment(resident_id, payment_method, description, confirm_method, amount)
        
        @staticmethod
        def get_payment_by_id(payment_id):
            return PaymentService.get_payment_by_id(payment_id)
        
        @staticmethod
        def get_all_payments():
            return PaymentService.get_all_payments()
        
        @staticmethod
        def finish_payment(payment_id):
            return PaymentService.finish_payment(payment_id)