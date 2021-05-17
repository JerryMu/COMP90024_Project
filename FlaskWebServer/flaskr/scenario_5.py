from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/scenario_5', methods=['GET', 'POST'])
def scenario_5():
    return render_template('scenario-5.html')