# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Form model creation and setup.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    """
    Form for adding a new pet.
    """

    name = StringField("Pet name",
                       validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(), AnyOf({"cat", "dog", "porcupine"})])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = IntegerField("Age (years)",
                       validators=[NumberRange(0, 30)])
    notes = TextAreaField("Notes",
                          validators=[Optional()])
