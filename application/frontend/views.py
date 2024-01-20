from flask import (
    Blueprint,
    render_template,
    current_app
)

frontend = Blueprint('frontend', __name__, template_folder='templates')

@frontend.route('/')
@frontend.route('/index')
def index():
	return render_template('index.html')
