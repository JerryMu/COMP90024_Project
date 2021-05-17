from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/scenario_4', methods=['GET', 'POST'])
def scenario_4():
    return render_template('scenario-4.html')