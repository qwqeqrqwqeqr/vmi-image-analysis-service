from flask import Flask

from router import analysis, base, image

app = Flask(__name__)


app.register_blueprint(analysis.blue_print)
app.register_blueprint(image.blue_print)
app.register_blueprint(base.blue_print)

