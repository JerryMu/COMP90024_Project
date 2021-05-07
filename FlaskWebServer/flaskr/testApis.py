import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Test get success'
    else:
        return 'Methods not implemented'
