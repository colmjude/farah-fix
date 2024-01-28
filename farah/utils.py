import csv
import os

from application.models import Product


def create_csv(filename, _dir, header_row):
    # make sure the directory exists
    if not os.path.exists(_dir):
        os.makedirs(_dir)

    if not os.path.exists(filename):
        # Create the file and write the header row
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header_row)


def get_product_record(product_json):
    return Product.query.filter(Product.farah_product_id == product_json["id"]).first()
