from app import db
import enum

class Departament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.Integer, unique=True, nullable=False)
    administrator = db.relationship('Administrator', backref='departament', lazy=True)
    resident = db.relationship('Resident', backref='departament', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'address': self.address,
            'number': self.number,
            'administrator': self.administrator,
            'resident': self.resident
        }
    
class PaymentMethodEnum(enum.Enum):
    efectivo = 'efectivo'
    tarjeta = 'tarjeta'
    transferencia = 'transferencia'
    cheque = 'cheque'

class ConfirmMerthodEnum(enum.Enum):
    manual = 'manual'
    automatico = 'automatico'

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    payment_method = db.Column(db.Enum(PaymentMethodEnum), nullable=False)
    common_expense = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    confirm_method = db.Column(db.Enum(ConfirmMerthodEnum), nullable=False)
    recipe = db.relationship('Recipe', backref='payment', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date,
            'recipe': [
                {
            'id': recipe.id,
            'status': recipe.status.value,
            'last_payment': recipe.last_payment,
            'balance_due': recipe.balance_due,
            'resident': recipe.resident_id,
            'payment': recipe.payment_id
                }
                for recipe in self.recipe
            ]
        }


class StatusEnum(enum.Enum):
    pendiente = 'pendiente'
    en_proceso = 'en proceso'
    finalizado = 'finalizado'

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default=StatusEnum.pendiente)
    last_payment = db.Column(db.DateTime, nullable=False)
    balance_due = db.Column(db.Integer, nullable=False)
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.id'), nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'status': self.status,
            'last_payment': self.last_payment,
            'balance_due': self.balance_due,
            'resident': self.resident_id,
            'payment': self.payment_id
        }