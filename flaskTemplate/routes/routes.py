from flaskTemplate.routes import routes_bp

from flask import render_template


@routes_bp.route('/', methods=['GET', 'POST'])
def index():

    return render_template("index.html")