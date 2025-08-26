# from utility.validation import validate_email,validate_phone
# from utility.validation import login_required
from models.users import Rider, Driver
from db_connection import insert_data,find_user_by_email
from utility.response import response


# @login_required
class RiderController:
    def __init__(self,db):
        self.db = db

    def ride_profile(self,email):
        rider = find_user_by_email(self.db,email)
        if not rider:
            return response(False,"User not found",404)
        rider_copy = rider.copy()
        sensitive_fields = ["password","_id","ride_history","payment_method"]
        
        for field in sensitive_fields:
            rider_copy.pop(field, None)
            
        return response(True,"Rider Profile fetched",rider_copy,200)