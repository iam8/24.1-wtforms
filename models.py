# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Database model creation and setup.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CheckConstraint

DEFAULT_IMG = """https://i1.wp.com/thefamilysupportcenter.org/wp-content/uploads/2018/04/
kisspng-dog-paw-cougar-drawing-clip-art-paw-prints-5ad0eba3679bd0.8414908415236412514244.png"""
db = SQLAlchemy()


def connect_db(app):
    """
    Connect the given Flask application (app) to SQLA database.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """
    Model for a pet available for adoption.
    """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, server_default=DEFAULT_IMG)
    age = db.Column(db.Float, CheckConstraint("age >= 0"))
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, server_default="True")
