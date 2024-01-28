import uuid
from decimal import ROUND_HALF_UP, Decimal

from helpers.model_utils import GetOrCreateMixin, UpdateMixin
from sqlalchemy.orm import mapped_column

from application.extensions import db


def _generate_uuid():
    return uuid.uuid4()


class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)
    product_base_url = db.Column(db.String(255))


class Product(GetOrCreateMixin, UpdateMixin, db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    farah_product_id = db.Column(db.String)
    slug = db.Column(db.String)
    rrp = db.Column(db.Numeric(10, 2))
    product_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    entry_date = db.Column(db.Date, default=db.func.current_date())
    farah_published_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    company = db.relationship("Company")

    prices = db.relationship(
        "Price",
        back_populates="product",
        order_by="Price.collected_at",
    )

    def current_price(self):
        return self.prices[-1].price

    def last_price_check(self):
        return self.prices[-1].collected_at

    def discounted_by(self):
        return 100 - ((self.current_price() / self.rrp) * 100)

    def price_has_changed(self, current_price):
        # make sure price value is a Decimal
        if not isinstance(current_price, Decimal):
            current_price = Decimal(str(current_price)).quantize(
                Decimal("0.00"), rounding=ROUND_HALF_UP
            )
        if len(self.prices):
            if self.prices[-1].price == current_price:
                return False
        # will return true if no price yet recorded or price has changed
        return True

    def as_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "rrp": float(self.rrp),  # Convert Numeric to float
            "type": self.product_type,
        }


class Price(db.Model):
    __tablename__ = "price"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(10, 2))
    collected_at = db.Column(db.DateTime, default=db.func.now(), index=True)
    farah_discount = db.Column(db.String)

    product_id = mapped_column(db.ForeignKey("product.id", name="fk_price_product_id"))
    product = db.relationship("Product")
