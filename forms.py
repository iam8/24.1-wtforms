# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Form model creation and setup.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField


class AddPetForm(FlaskForm):
    """
    Form for adding a new pet.
    """

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age (years)")
    notes = TextAreaField("Notes")
    available = SelectField("Available (Y/N)")
