from flask import Flask

from router import analysis, base

app = Flask(__name__)


app.register_blueprint(analysis.blue_print)
app.register_blueprint(base.blue_print)

