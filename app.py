# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Main Flask application.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm


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
    > Displays form to add a new pet
    > Validates a new pet
    > Creates and adds the new pet
    """

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet()
        form.populate_obj(new_pet)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    return render_template("pet_add_form.jinja2", form=form)

# -------------------------------------------------------------------------------------------------


# MAIN --------------------------------------------------------------------------------------------

if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False)
