import logging
import sys

import click
from farah.fetch import extract_products_from_files, fetch_pages
from farah.loader import reconcile_products
from farah.price import insert_latest_prices
from flask.cli import AppGroup, with_appcontext

from application.models import Company

# similar to what we used on development plan prototype
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


data_cli = AppGroup("data")
product_cli = AppGroup("product")
price_cli = AppGroup("price")


@click.command()
@with_appcontext
def load():
    print("This is a command")


@data_cli.command("init")
def init_data():
    from application.extensions import db

    farah = {
        "name": "Farah",
        "website": "https://www.farah.co.uk/",
        "product_base_url": "https://www.farah.co.uk/collections/clothing/products/",
    }

    record = Company(**farah)

    db.session.add(record)
    db.session.commit()


@product_cli.command("fetch")
def fetch_products():
    fetch_pages(1)


@product_cli.command("insert")
def insert_products():
    # TODO: add check that pages have been fetched
    products = extract_products_from_files()

    reconcile_products(products)


@price_cli.command("latest")
def latest_prices():
    # TODO: add check that pages have been fetched
    products = extract_products_from_files()

    insert_latest_prices(products)
