from models.users import User,Rider,Driver

def user_to_dict(user_obj, hashed_password):
        """Convert Rider/Driver object to dictionary for MongoDB"""
        data = {
            "user_id": user_obj.user_id,
            "full_name": user_obj.full_name,
            "email": user_obj.email,
            "phone": user_obj.phone,
            "role": user_obj.role,
            "password": hashed_password,
            "created_at": user_obj.created_at
        }
        if isinstance(user_obj, Rider):
            data["payment_method"] = user_obj.payment_method
            data["ride_history"] = user_obj.ride_history
        elif isinstance(user_obj, Driver):
            # Vehicle is optional
            data["vehicle"] = vars(user_obj.vehicle) if user_obj.vehicle else None
            data["is_available"] = user_obj.is_available
        return data