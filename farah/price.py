from farah.logger import log_price_change
from farah.utils import get_product_record

from application.extensions import db
from application.models import Price


def insert_price(product_obj, product_json):
    price = Price()
    price.price = product_json["price_max_gbp"]
    price.farah_discount = product_json["percent_sale_min_gbp"]
    product_obj.prices.append(price)

    db.session.add(product_obj)
    db.session.commit()


def insert_latest_prices(products):
    for product in products.values():
        product_obj = get_product_record(product)
        current_price = product["price_max_gbp"]
        if product_obj.price_has_changed(current_price):
            insert_price(product_obj, product)
            log_price_change(product_obj)
