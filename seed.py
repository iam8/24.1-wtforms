# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Seed file that adds initial pet data into adoption agency database.

WARNING: this file will delete all existing data in the database before adding seed data.
"""

from models import db, Pet
from app import app, connect_db

IMG1 = ("https://images.creativemarket.com/0.1.0/ps/5990225/910/1055/m2/fpnw/wm1/"
        + "x8ffga7ec6bixlnocldho4pp8wqetmujxpzuvywgnaapnlrwbrx8rrnk70dsduch-.jpg?1551724001&"
        + "s=2e61d2b6994c17d8856eb15af1915236")
IMG2 = "https://www.zoochat.com/community/media/african-crested-porcupine.342328/full?d=1478839075"
IMG3 = "https://i.pinimg.com/736x/7e/be/7a/7ebe7ad8f4511ac6c4e33b6810788bd9.jpg"


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
                   is_available=True,
                   photo_url=IMG1)

        pricky = Pet(name="Pricky",
                     species="Porcupine",
                     age=5,
                     notes="Watch out. He bites.",
                     is_available=True,
                     photo_url=IMG2)

        gideon = Pet(name="Gideon",
                     species="Cat",
                     age=10,
                     is_available=False,
                     photo_url=IMG3)

        db.session.add_all([spot, pricky, gideon])
        db.session.commit()
