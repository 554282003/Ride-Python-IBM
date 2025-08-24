import bcrypt

def hash_password(password):
    """Strong private method to hash password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())