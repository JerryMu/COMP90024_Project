from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@bp.route('/welcome_page', methods=['GET', 'POST'])
def welcome_page():

    return render_template('welcome-page.html')


@bp.route('/scenario_1', methods=['GET', 'POST'])
def scenario_1():
    return render_template('scenario-1.html')


@bp.route('/scenario_2', methods=['GET', 'POST'])
def scenario_2():
    return render_template('scenario-2.html')


@bp.route('/scenario_3', methods=['GET', 'POST'])
def scenario_3():
    return render_template('scenario-3.html')


@bp.route('/scenario_4', methods=['GET', 'POST'])
def scenario_4():
    return render_template('scenario-4.html')


@bp.route('/scenario_5', methods=['GET', 'POST'])
def scenario_5():
    return render_template('scenario-5.html')