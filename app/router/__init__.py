from flask import Flask

from router import analysis, base

app = Flask(__name__)


app.register_blueprint(analysis.blue_print)
app.register_blueprint(base.blue_print)





    # image= get_patient_image(5)
    #
    # return render_template('index.html',image="http://106.245.10.197:2323/"+image.a_10)
    #
