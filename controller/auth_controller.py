import json
from models.users import Rider, Driver
from functools import wraps
from db_connection import insert_data, find_user_by_email
from utility.user_to_dic import user_to_dict
from utility.hashing import hash_password, check_password
from utility.validation import validate_email, validate_phone
from utility.response import response

def login_required(func):
    """Decorator to ensure user is logged in."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._current_user:
            return response(False, "User not logged in", status_code=401)
        return func(self, *args, **kwargs)
    return wrapper

def role_required(role):
    """Decorator to ensure current user has required role."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._current_user or self._current_user.get("role") != role:
                return response(False, f"Access denied! Requires role: {role}", status_code=403)
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

# -------------- AuthController Class ----------------
class AuthController:
    def __init__(self, db):
        self._current_user = None
        self.db = db

    # ---------------- Public Methods ----------------
    def signup(self, user_id, full_name, email, phone, role, password):
        """Create a new Rider or Driver."""
        if not all([user_id, full_name, email, phone, role, password]):
            return response(False, "All fields are required", status_code=400)
        
        if not validate_email(email) or not validate_phone(phone):
            return response(False, "Invalid email or phone", status_code=400)
        
        if find_user_by_email(self.db, email):
            return response(False, "User already exists", status_code=409)
        
        hashed_password = hash_password(password)
        
        if role.lower() == 'rider':
            user_obj = Rider(user_id, full_name, email, phone)
        elif role.lower() == 'driver':
            user_obj = Driver(user_id, full_name, email, phone)
        else:
            return response(False, "Invalid role", status_code=400)
        
        final_user = user_to_dict(user_obj, hashed_password)
        inserted_id = insert_data(self.db, final_user)
        
        return response(True, f"New user created", {"user_id": inserted_id}, status_code=201)

    def login(self, email, password):
        """Verify credentials and set _current_user."""
        if not validate_email(email):
            return response(False, "Invalid Email", status_code=400)
        
        user = find_user_by_email(self.db, email)
        if not user:
            return response(False, "User not found", status_code=404)
        
        if not check_password(password, user["password"]):
            return response(False, "Incorrect password", status_code=401)
        
        self._current_user = user
        user_copy = user.copy()
        user_copy.pop("password", None)  # remove sensitive info
        return response(True, "Login successful", user_copy, status_code=200)

    @login_required
    def logout(self):
        """Logout the current user."""
        self._current_user = None
        return response(True, "User logged out successfully", status_code=200)
