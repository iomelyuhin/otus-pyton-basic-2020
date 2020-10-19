from flask import Flask, request

from views import catalog_app

app = Flask(__name__)
app.register_blueprint(catalog_app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return f"<h1>Hello, {request.form.get('name', 'World')}!</h1>"
    return "Hello world"


# @app.route("/catalog", methods=["GET", "POST"])
# def catalog():
#     return f"<h1>Catalog</h1>"
