from datetime import datetime


class Payment:
    def __init__(self, amount=0.0, method="cash", status="pending", payment_date=None):
        self.amount = amount
        self.method = method
        self.status = status
        self.payment_date = payment_date or None

    def __repr__(self):
        return f"<Payment {self.amount} {self.method} ({self.status})>"


class Rating:
    def __init__(self, given_by, given_to, score, comment=""):
        self.given_by = given_by
        self.given_to = given_to
        self.score = score
        self.comment = comment

    def __repr__(self):
        return f"<Rating {self.score}/5 from {self.given_by} → {self.given_to}>"


class Ride:
    def __init__(
        self,
        ride_id,
        rider_id,
        driver_id,
        vehicle_id,
        pickup_location,
        drop_location,
        status="requested",
        fare=0.0,
        ride_date=None,
        payment=None,
        ratings=None
    ):
        self.ride_id = ride_id
        self.rider_id = rider_id
        self.driver_id = driver_id
        self.vehicle_id = vehicle_id
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.status = status
        self.fare = fare
        self.ride_date = ride_date or datetime.now()

        # Use Payment and Rating objects
        self.payment = payment if payment else Payment(amount=fare)
        self.ratings = ratings if ratings else []

    def __repr__(self):
        return f"<Ride {self.ride_id} - {self.pickup_location} → {self.drop_location} ({self.status})>"
