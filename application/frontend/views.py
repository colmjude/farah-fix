import requests
from flask import Blueprint, render_template, request

from application.models import Company, Product

frontend = Blueprint("frontend", __name__, template_folder="templates")


@frontend.route("/")
@frontend.route("/index")
def index():
    farah = Company.query.get(1)
    product = None
    url_check = None

    if request.method == "GET" and request.args.get("id"):
        product = Product.query.get(int(request.args.get("id")))
        response = requests.get(f"{farah.product_base_url}{product.slug}")
        url_check = response.status_code

    return render_template(
        "index.html", farah=farah, product=product, url_check=url_check
    )
