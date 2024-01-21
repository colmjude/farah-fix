import uuid

from datetime import datetime

from application.extensions import db


def _generate_uuid():
    return uuid.uuid4()


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)
    product_base_url = db.Column(db.String(255))


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    slug = db.Column(db.String)
    rrp = db.Column(db.Numeric(10, 2))
    product_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    entry_date = db.Column(db.Date, default=db.func.current_date())
    farah_published_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    company_id = db.Column(
        db.Integer, db.ForeignKey("company.id")
    )

    def as_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'rrp': float(self.rrp),  # Convert Numeric to float
            'type': self.product_type
        }
