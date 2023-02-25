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
                       validators=[InputRequired()],
                       render_kw={"placeholder": "Enter a pet name"})
    species = StringField("Species",
                          validators=[InputRequired(), AnyOf({"cat", "dog", "porcupine"})],
                          render_kw={"placeholder": "Enter a species"})
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()],
                            render_kw={"placeholder": "Optional - enter a URL to a photo"})
    age = FloatField("Age (years)",
                     validators=[Optional(), NumberRange(0, 30)],
                     render_kw={"placeholder": "Optional - enter an age (0-30, inclusive)"})
    notes = TextAreaField("Notes",
                          validators=[Optional()],
                          render_kw={"placeholder": "Optional - add any notes about this pet"})


class EditPetForm(FlaskForm):
    """
    Form for editing an existing pet.
    """

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()],
                            render_kw={"placeholder": "Optional - enter a URL to a photo"})
    notes = TextAreaField("Notes",
                          validators=[Optional()],
                          render_kw={"placeholder": "Optional - add any notes about this pet"})
    is_available = RadioField("Available for adoption?",
                              choices=[("True", "Yes"), ("False", "No")])
