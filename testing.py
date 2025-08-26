import datetime

dc = {'success': True, 'message': 'Rider Profile fetched', 'data': {'user_id': 1006, 'full_name': 'Vivek Vishvakarma', 'email': 'vivek5542810@gmail.com', 'phone': '+91-9104519374', 'role': 'rider', 'password': '$2b$12$DHs.oNGvFlBZbEhTshLHaeO7B2HJRfBipFXw9pM34yH0vhEhXd586', 'created_at': datetime.datetime(2025, 8, 26, 11, 23, 48, 638000), 'payment_method': 'cash', 'ride_history': []}, 'status_code': 200, 'timestamp': '2025-08-26T07:24:27.293682'}

bc = dc.get('data').pop('user_id')
print(bc)