# -*- coding: utf-8 -*-
import os


class Config(object):
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_ROOT, os.pardir))
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # currently pointing to a sqlite db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(PROJECT_ROOT, 'products.db')


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
