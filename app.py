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

app.config["SQALCHEMY_DATABASE_URI"] = "postresql:///adoption"




# MAIN --------------------------------------------------------------------------------------------

if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
