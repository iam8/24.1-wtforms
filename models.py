# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Database model creation and setup.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """
    Connect the given Flask application (app) to SQLA database.
    """

    db.app = app
    db.init_app()
