from db_connection import connect_to_db
from controller.auth_controller import AuthController
from models.users import Rider, Driver
# from models.vehicle import Vehicle

def main():
    # 1. Connect to database
    db = connect_to_db()

    # 2. Initialize controllers
    auth_ctrl = AuthController(db)

    # 3. Example: Signup a new rider
    signup_response = auth_ctrl.signup(
        user_id=1011,
        full_name="Vikram Vishwakarma",
        email="vikramVish@example.com",
        phone="+91-9876543210",
        role="Rider",
        password="securepassword"
    )
    print(signup_response)

    login_response = auth_ctrl.login(email="vikramVish@example.com",password="securepassword")
    print(login_response)

    auth_ctrl.logout()

    # # 4. Example: Signup a new driver (without vehicle)
    # signup_response = auth_ctrl.signup(
    #     id=1005,
    #     full_name="Rohit Sharma",
    #     email="rohit@example.com",
    #     phone="+919812345678",
    #     role="Driver",
    #     password="strongpassword"
    # )
    # print(signup_response)

    # 5. Later, driver can add a vehicle (optional step)
    # driver_obj = fetch_driver_from_db(...)  # hypothetical
    # driver_obj.add_vehicle(vehicle_id=158, make="Maruti Suzuki", model="XUV500", year=2019, reg_no="MH78QG9059", color="Blue")
    # update_driver(db, driver_obj)

if __name__ == "__main__":
    main()
