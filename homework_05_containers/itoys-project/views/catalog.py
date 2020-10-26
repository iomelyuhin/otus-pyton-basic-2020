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
    products = Product.query.filter_by(deleted=False).order_by(Product.id).all()

    return render_template("catalog/index.html", products=products)


@catalog_app.route("/catalog/<int:product_id>", methods=["DELETE"])
def catalog_delete(product_id=None):
    products = Product.query.filter_by(deleted=False).all()
    product = Product.query.filter_by(id=product_id).one_or_none()
    if request.method == "DELETE":
        product.deleted = True
        db.session.commit()
        return jsonify(ok=True)

    return render_template("catalog/index.html", products=products)


@catalog_app.route("/catalog/<int:product_id>", methods=["POST"])
def catalog_duplicate(product_id=None):
    products = Product.query.filter_by(deleted=False).all()
    product = Product.query.filter_by(id=product_id).one_or_none()
    if request.method == "POST":
        new_product = Product(
            name=product.name,
            description=product.description,
            img_href=product.img_href,
            price=product.price,
            is_sale=product.is_sale,
            deleted=product.deleted,
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(ok=True)

    return render_template("catalog/index.html", products=products)

