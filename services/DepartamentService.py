from models.DepartamentModel import db, Departament, Payment, Recipe, StatusEnum
import datetime

class DepartamentService:

    @staticmethod
    def create_departament(data):
        departament = Departament(
            address=data['address'],
            number=data['number']
        )
        db.session.add(departament)
        db.session.commit()
        return departament
    
    @staticmethod
    def get_departament_by_id(departament_id):
        return Departament.query.get(departament_id)
    
    @staticmethod
    def get_all_departaments():
        return Departament.query.all()
    
class PaymentService:

    @staticmethod
    def create_payment(resident_id, payment_method, description, confirm_method, amount):
        payment = Payment(
            amount=amount,
            date=datetime.datetime.now(),
            payment_method=payment_method,
            common_expense=amount,
            description=description,
            confirm_method=confirm_method
        )

        db.session.add(payment)
        db.session.commit()

        recipe = Recipe(
            status=StatusEnum.pendiente,
            last_payment=datetime.datetime.now(),
            balance_due=amount,
            resident_id=resident_id,
            payment_id=payment.id
        )
        db.session.add(recipe)
        db.session.commit()
        return payment
    
    @staticmethod
    def get_payment_by_id(payment_id):
        return Payment.query.get(payment_id)
    
    @staticmethod
    def get_all_payments():
        return Payment.query.all()
    
    @staticmethod
    def finish_payment(payment_id):
        payment = Payment.query.get(payment_id)
        recipe = Recipe.query.filter_by(payment_id=payment_id).first()
        print(recipe)
        recipe.status = StatusEnum.finalizado
        db.session.commit()
        return payment
    
