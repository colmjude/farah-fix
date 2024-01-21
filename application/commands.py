import sys
import click
import logging

from flask.cli import AppGroup
from flask.cli import with_appcontext
from application.models import Company

# similar to what we used on development plan prototype
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


data_cli = AppGroup("data")


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

