from datetime import datetime

class User:
    def __init__(self,user_id,full_name,email,phone,role):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.role = role
        self.created_at = datetime.now()

    # def __repr__(self):
    #     return f"<User {self.user_id} - {self.full_name} ({self.role})>"
    
class Rider(User):
    def __init__(self, user_id, full_name, email, phone, payment_method="cash"):
        super().__init__(user_id, full_name, email, phone, role="rider")
        self.payment_method = payment_method
        self.ride_history = []

class Vehicle:
    def __init__(self, vehicle_id, make, model, year, registration_number, color):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.registration_number = registration_number
        self.color = color

class Driver(User):
    def __init__(self, user_id, full_name, email, phone):
        super().__init__(user_id, full_name, email, phone, role="driver")
        self.vehicle = None
        self.is_available = True

    def add_vehicle(self, vehicle_id, make, model, year, reg_no, color):
        self.vehicle = Vehicle(vehicle_id, make, model, year, reg_no, color)
        
# user = User(1,"vivek","vivek@gmail.com",9104519364,"rider")
# print(user.__repr__())