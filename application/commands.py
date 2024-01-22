import sys
import click
import logging

from flask.cli import AppGroup
from flask.cli import with_appcontext
from application.models import Company
from farah.fetch import fetch_pages, extract_products_from_files

# similar to what we used on development plan prototype
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


data_cli = AppGroup("data")
product_cli = AppGroup("product")


@click.command()
@with_appcontext
def load():
    print("This is a command")


@data_cli.command("init")
def init_data():
    from application.extensions import db

    farah = {
        "name": 'Farah',
        "website": 'https://www.farah.co.uk/',
        "product_base_url": 'https://www.farah.co.uk/collections/clothing/products/'
    }

    record = Company(**farah)

    db.session.add(record)
    db.session.commit()


@product_cli.command("fetch")
def fetch_products():
    fetch_pages(1)


@product_cli.command("extract")
def extract_products():
    # TODO: add check that pages have been fetched
    products = extract_products_from_files()
    # loop over all products
    for index, (k, product) in enumerate(products.items()):
        if product["available"] is not False:
            print(
                f'{index+1}. {product["title"]} [{product["product_type"]}] ({product["id"]}) - {product["available"]}'
            )
            print(
                f'pmax: {product["price_max_gbp"]}, pmin: {product["price_min_gbp"]}, cmax: {product["compare_at_price_max_gbp"]}, cmin: {product["compare_at_price_min_gbp"]}, %: {product["percent_sale_min_gbp"]}'
            )
