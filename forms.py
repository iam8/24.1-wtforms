# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Form model creation and setup.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, RadioField
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
    age = FloatField("Age (years)",
                     validators=[Optional(), NumberRange(0, 30)])
    notes = TextAreaField("Notes",
                          validators=[Optional()])


class EditPetForm(FlaskForm):
    """
    Form for editing an existing pet.
    """

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    notes = TextAreaField("Notes",
                          validators=[Optional()])
    available = RadioField("Available for adoption?",
                           choices=[("True", "Yes"), ("False", "No")])
