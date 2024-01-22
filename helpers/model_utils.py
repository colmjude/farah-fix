from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from application.extensions import db


class GetOrCreateMixin(object):
    @classmethod
    def get_or_create(cls, **kwargs):
        try:
            return cls.query.filter_by(**kwargs).one(), False

        except NoResultFound:
            obj = cls(**kwargs)
            db.session.add(obj)
            db.session.commit()
            return obj, True

        except MultipleResultsFound:
            raise


class UpdateMixin(object):
    def update(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                print("set property")
                setattr(self, key, val)

        db.session.add(self)
        db.session.commit()
