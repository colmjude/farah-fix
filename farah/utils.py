from application.models import Product


def get_product_record(product_json):
    return Product.query.filter(Product.farah_product_id == product_json["id"]).first()
