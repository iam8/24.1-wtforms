# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Seed file that adds initial pet data into adoption agency database.

WARNING: this file will delete all existing data in the database before adding seed data.
"""

from models import db, Pet
from app import app, connect_db


if __name__ == "__main__":

    connect_db(app)

    # Drop and create all tables
    with app.app_context():
        db.drop_all()
        db.create_all()

        Pet.query.delete()

        # Create pets
        spot = Pet(name="Spot",
                   species="Dog",
                   age=1,
                   notes="Cute and cuddly Beagle puppy",
                   is_available=True)

        pricky = Pet(name="Pricky",
                     species="Porcupine",
                     age=5,
                     notes="Watch out. He bites.",
                     is_available=True)

        gideon = Pet(name="Gideon",
                     species="Cat",
                     age=10,
                     is_available=False)

        db.session.add_all([spot, pricky, gideon])
        db.session.commit()
