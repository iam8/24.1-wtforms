# Ioana A Mititean
# 24.1 Exercise: WTForms
# Pet Adoption Agency

"""
Main Flask application.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db


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

    return render_template("home.jinja2")

# -------------------------------------------------------------------------------------------------


# MAIN --------------------------------------------------------------------------------------------

if __name__ == "__main__":

    print("In main block of app.py")
    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False)
