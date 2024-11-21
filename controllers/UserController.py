from services.UserService import ResidentService, AdministratorService

class ResidentController:

    @staticmethod
    def create_resident_controller(data):
        return ResidentService.create_resident(data)
    
    @staticmethod
    def get_resident_by_id_controller(resident_id):
        return ResidentService.get_resident_by_id(resident_id)
    
    @staticmethod
    def get_all_residents_controller():
        return ResidentService.get_all_residents()
    
class AdministratorController:

    @staticmethod
    def create_administrator_controller(data):
        return AdministratorService.create_administrator(data)
    
    @staticmethod
    def get_administrator_by_id_controller(administrator_id):
        return AdministratorService.get_administrator_by_id(administrator_id)
    
    @staticmethod
    def get_all_administrators_controller():
        return AdministratorService.get_all_administrators()