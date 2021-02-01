from flask import Blueprint
from flask_restful import Api

from .hero import Hero

def setup_blueprint():
    blueprint = Blueprint(
        "superhero", __name__,
    )

    api = Api(blueprint)
    api.add_resource(Hero, "/hero")
    return blueprint
