import os


class Config:
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:SQL2610@localhost:5432/DHotel"

    DEBUG = True
    SECRET_KEY = "chocolate"


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")

    SECRET_KEY = os.environ.get("SECRET_KEY", "")

    DEBUG = False

# Define an env variable called "FLASK_ENV" and assign it to "dev" in your laptop and to "prod" in
# your server

config = {
    "development": DevConfig,
    "prod": ProdConfig,
}
