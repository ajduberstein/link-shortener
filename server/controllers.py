from flask import (
    jsonify,
    render_template,
    redirect,
    request,
    Blueprint,
)


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Main"

@main.route('/react', methods = ['GET'])
def react():
    return render_template('main.htm')

@main.route('/<int:urlid>', methods = ['GET'])
def reroute(urlid):
    """
    Sends user to the linked site

    Retrieves the site from our SQL store
    """
    return redirect("https://www.google.com", code=302)

@main.route('/link', methods = ['POST'])
def add_url():
    return

@main.errorhandler(404)
def page_not_found(e):
    #snip
    return render_template('404.htm'), 404
