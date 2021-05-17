from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/welcome_page', methods=['GET', 'POST'])
def welcome_page():
    return render_template('welcome-page.html')