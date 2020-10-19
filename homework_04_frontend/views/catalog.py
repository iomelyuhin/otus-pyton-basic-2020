from flask import Blueprint, render_template

catalog_app = Blueprint("catalog_app", __name__)


@catalog_app.route("/catalog")
def catalog_list():
    return render_template("catalog/index.html")
