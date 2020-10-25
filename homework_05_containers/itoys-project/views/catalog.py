from flask import Blueprint, render_template, request, jsonify
from models import db, Product

catalog_app = Blueprint("catalog_app", __name__)

PRODUCTS = {
    1: "Развивающие книги",
    2: "Конструкторы",
    3: "Раскраски"
}


@catalog_app.route("/catalog", methods=["GET", "DELETE"])
def catalog_list():
    products = Product.query.filter_by(deleted=False).all()

    return render_template("catalog/index.html", products=products)


@catalog_app.route("/catalog/<int:product_id>", methods=["DELETE"])
def catalog_delete(product_id=None):
    products = Product.query.filter_by(deleted=False).all()
    product = Product.query.filter_by(id=product_id).one_or_none()
    if request.method == "DELETE":
        print("Product id = ", product_id)
        product.deleted = True
        db.session.commit()
        return jsonify(ok=True)

    return render_template("catalog/index.html", products=products)


@catalog_app.route("/catalog/<int:product_id>", methods=["POST"])
def catalog_duplicate(product_id=None):
    products = Product.query.filter_by(deleted=False).all()
    product = Product.query.filter_by(id=product_id).one_or_none()
    if request.method == "POST":
        db.session.add(product)
        db.session.commit()
        return jsonify(ok=True)

    return render_template("catalog/index.html", products=products)

