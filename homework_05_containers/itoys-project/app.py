from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config
from views import index_app
from views import catalog_app
from views import contact_app

app = Flask(__name__)
app.register_blueprint(index_app)
app.register_blueprint(catalog_app)
app.register_blueprint(contact_app)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET", "POST"])
def index():
    name = "World"
    if request.method == "POST":
        name = request.form.get('name', 'World')
    return render_template("index.html", name=name)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

