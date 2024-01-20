import uuid

from datetime import datetime

from application.extensions import db


def _generate_uuid():
    return uuid.uuid4()

