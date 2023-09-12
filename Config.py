import os


basedir = os.path.abspath(os.path.diename(__file__))
class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get("DOUMBOUYAH") OR "THIS IS MY SECRET-KEY DOU"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///" + os.path.join(basedir, app.db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "amazing-api"
    UPLOAD_IMAGES_DEST = os.path.join("ststic", "images")
    MAX_CONTANT_LENGTH = 10*1024*1024  
    