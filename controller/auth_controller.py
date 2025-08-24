from models.users import User, Rider, Driver, Vehicle
from functools import wraps
import re
from db_connection import insert_data,find_user_by_email
from utility.user_to_dic import user_to_dict
from utility.hashing import hash_password,check_password
from utility.validation import validate_email,validate_phone

# ---------------- Decorators ----------------
def login_required(func):
    """Decorator to ensure user is logged in."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._current_user:
            print("User not logged in!")
            return None
        return func(self, *args, **kwargs)
    return wrapper

def role_required(role):
    """Decorator to ensure current user has required role."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._current_user or self._current_user.role != role:
                print(f"Access denied! Requires role: {role}")
                return None
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

# -------------- AuthController Class ----------------
class AuthController:
    def __init__(self,db):
        self._current_user = None  # private attribute
        self.db = db

    # ---------------- Public Methods ----------------
    def signup(self, user_id ,full_name, email, phone, role, password):
        """
        Create a new Rider or Driver.
        Validate input and hash password internally.
        Save to DB.
        """
        if not all([user_id, full_name, email, phone, role, password]):
            return "All fields required!!!"
        
        check_email = validate_email(email)
        check_user_exist = find_user_by_email(self.db,email)
        if check_user_exist:
            return "User already Exist"
        
        check_phone = validate_phone(phone)
        if(not check_email or not check_phone):
            return "Invalid email or phone"

        hashed_password = hash_password(password)
        
        if role.lower() == 'rider':
            user_obj = Rider(user_id,full_name,email,phone)
        elif role.lower() == 'driver':
            user_obj = Driver(user_id,full_name,email,phone)
        else:
            return "invalid role"
        print(user_obj.user_id)
        final_user = user_to_dict(user_obj,hashed_password)
        inserted_id = insert_data(self.db,final_user)

        return f"New user created : Id is {inserted_id}"


    def login(self, email, password):
        """
        Verify credentials and set _current_user
        """
        check_email = validate_email(email)
        if not check_email:
            return "Invalid Email"
        
        user = find_user_by_email(self.db,email)
        if not user:
            return "User Not Found"
        
        check_password_value = check_password(password,user["password"])
        
        if(not check_password_value):
            return "Password is incorrect!!!"

        self._current_user = user
        return f"{user['user_id']} is logged in"

    @login_required
    def logout(self):
        """Logout the current user"""
        self._current_user = None
        print("User logged out.")