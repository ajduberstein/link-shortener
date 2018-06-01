from flask import (
    # jsonify,
    render_template,
    redirect,
    request,
    Blueprint,
)

from .models import Link

# import base58


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('main.htm')


@main.route('/<int:urlid>', methods=['GET'])
def reroute(urlid):
    """
    Sends user to the linked site

    Retrieves the site from our SQL store
    """
    # urlid = base58.b58decode(str(b58urlid))  # noqa
    url = Link.get(urlid)
    if url:
        return redirect(url, code=302)
    return redirect('/', code=302)


@main.route('/link', methods=['POST'])
def add_url():
    data = request.get_data()
    url = data['url']
    ok = Link.add(url)
    if ok:
        return 'OK', 201
    return '', 304


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.htm'), 404
