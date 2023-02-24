# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Main Flask application.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "O secreta foarte secreta"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption"


# HOMEPAGE ----------------------------------------------------------------------------------------

@app.route("/")
def homepage():
    """
    Homepage route. Displays a list of the pets currently at the adoption agency.
    """

    pets = Pet.query.all()
    return render_template("home.jinja2", pets=pets)

# -------------------------------------------------------------------------------------------------


# ADDING PETS -------------------------------------------------------------------------------------

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """
    Route for adding a new pet.

    This route:
        - Displays form to add a new pet
        - Validates user-entered form field values
        - Creates and adds the new pet (if validation successful)
    """

    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    return render_template("pet_add_form.jinja2", form=form)

# -------------------------------------------------------------------------------------------------


# EDITING PETS ------------------------------------------------------------------------------------

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def display_and_edit_pet(pet_id):
    """
    Route for displaying information about a pet with a given ID and for editing that pet.

    This route:
        - Displays information about the pet with the given ID
        - Displays an edit form for the pet with the given ID
        - Validates user-entered form field values
        - Updates the pet (if validation successful)
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

    return render_template("pet_display_and_edit.jinja2", form=form)

# -------------------------------------------------------------------------------------------------


# MAIN --------------------------------------------------------------------------------------------

if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False)
