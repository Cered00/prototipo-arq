from models.UserModel import db, Resident, Administrator

class ResidentService:
    @staticmethod
    def create_resident(data):
        resident = Resident(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
	    address=data['address'],
	    balance=data['balance'],
            departament_id=data['departament_id']
        )
        db.session.add(resident)
        db.session.commit()
        return resident
    
    @staticmethod
    def get_resident_by_id(resident_id):
        return Resident.query.get(resident_id)
    
    @staticmethod
    def get_all_residents():
        return Resident.query.all()
    

class AdministratorService:
    @staticmethod
    def create_administrator(data):
        administrator = Administrator(
            name=data['name'],
            email=data['email'],
            departament_id=data['departament_id']
        )
        db.session.add(administrator)
        db.session.commit()
        return administrator
    
    @staticmethod
    def get_administrator_by_id(administrator_id):
        return Administrator.query.get(administrator_id)
    
    @staticmethod
    def get_all_administrators():
        return Administrator.query.all()
