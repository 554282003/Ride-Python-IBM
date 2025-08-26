from db_connection import connect_to_db
from controller.auth_controller import AuthController
from controller.rider_controller import RiderController
from models.users import Rider, Driver
# from models.vehicle import Vehicle

def rider_menu(auth_ctrl, user, db):
    print("hi")
    ride_ctrl = RiderController(db)
    """Menu for Riders"""
    while True:
        print("\n=== Rider Menu ===")
        print("1. Book a Ride")
        print("2. View Ride History")
        print("3. Rider Profile")
        print("4. Logout")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            print(f"{user['full_name']} is booking a ride... (stub)")
        elif choice == "2":
            print(f"Showing ride history for {user['full_name']}... (stub)")
        elif choice == "3":
            print(f"showing rider profile:\n")
            print(ride_ctrl.ride_profile(user.get("email")))
        elif choice == "4":
            print(auth_ctrl.logout().get('message'))
            break
        else:
            print("Invalid choice. Try again.")


def driver_menu(auth_ctrl, user):
    """Menu for Drivers"""
    while True:
        print("\n=== Driver Menu ===")
        print("1. View Assigned Rides")
        print("2. Update Ride Status")
        print("3. Logout")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            print(f"{user['full_name']} is viewing assigned rides... (stub)")
        elif choice == "2":
            print(f"{user['full_name']} is updating ride status... (stub)")
        elif choice == "3":
            print(auth_ctrl.logout().get('message'))
            break
        else:
            print("Invalid choice. Try again.")


def main():
    # Connect to database
    db = connect_to_db()
    auth_ctrl = AuthController(db)

    print("\n=== Ride-Hailing CLI App ===")

    while True:
        print("\nChoose an option:")
        print("1. Signup (Rider/Driver)")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            # Signup flow
            user_id = int(input("Enter User ID: "))
            full_name = input("Enter Full Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            role = input("Enter Role (Rider/Driver): ")
            password = input("Enter Password: ")

            signup_response = auth_ctrl.signup(
                user_id=user_id,
                full_name=full_name,
                email=email,
                phone=phone,
                role=role,
                password=password
            )
            print("Signup Response:", signup_response)

        elif choice == "2":
            # Login flow
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            login_response = auth_ctrl.login(email=email, password=password)
            print(type(login_response))
            if login_response.get("success"):
                user = login_response['data']
                if user["role"].lower() == "rider":
                    print(login_response.get("message"))
                    rider_menu(auth_ctrl, user, db)
                elif user["role"].lower() == "driver":
                    driver_menu(auth_ctrl, user, db)
                else:
                    print("Unknown role. Cannot proceed.")
            else:
                print("Login failed:", login_response.get("message"))

        elif choice == "3":
            # Logout
            logout_response = auth_ctrl.logout()
            # print(logout_response,"login_response")

        elif choice == "4":
            print("Exiting app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
