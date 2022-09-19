from flask import app, Blueprint

blue_print = Blueprint("base", __name__, url_prefix="/")


@blue_print.route('/')
def base_url():
    return "default"


