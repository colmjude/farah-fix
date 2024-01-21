import uuid

from datetime import datetime

from application.extensions import db


def _generate_uuid():
    return uuid.uuid4()


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    slug = db.Column(db.String)
