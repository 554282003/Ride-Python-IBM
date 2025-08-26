import re 

def validate_email(email):
    """Internal helper for email format validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if(re.match(pattern,email)):
        return True
    return False

def validate_phone(phone):
    """Internal helper for phone format validation"""
    pattern = r'^\+[0-9]{2}-[0-9]{10}$'
    if(re.match(pattern,phone)):
        return True
    return False
