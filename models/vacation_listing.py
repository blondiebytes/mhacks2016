
class VacationListing(db.Model):
    __tablename__ = "vacation_listings"

    id = db.Column(db.Integer, primary_key=True)
    starting_location = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    departure_date = db.Column(db.Integer, nullable=False)

    listing_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing = db.relationship("User", back_populates="vacation_listings")
    reservations = db.relationship("Reservation", back_populates="vacation_listing")

    def __init__(self, starting_location, destination, cost, departure_date, listing):
        self.starting_location = starting_location
        self.destination = destination
        self.cost = cost
        self.departure_date = departure_date
        self.listing = listing

    def __repr__(self):
        return '<VacationListing %r %r %r %r>' % self.id, self.destination, self.cost, self.departure_date