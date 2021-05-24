from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.fetchCouchDB import get_db

CITIES = ["Sydney",
          "Melbourne",
          "Brisbane",
          "Perth (WA)",
          "Adelaide"]

bp = Blueprint('main', __name__, url_prefix='/main')


@bp.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@bp.route('/welcome_page', methods=['GET', 'POST'])
def welcome_page():

    return render_template('welcome-page.html')


@bp.route('/scenario_1', methods=['GET', 'POST'])
def scenario_1():
    scenario_1_db = get_db('scenario_1')
    # Total number of tweet mentioned COVID-19.
    tweet_mentions = scenario_1_db['ct_attention_covid']
    data = {
        'tweet_mentions_key': list(tweet_mentions.keys())[2:],
        'tweet_mentions_value': list(tweet_mentions.values())[2:]
    }
    return render_template('Scenario-1.html', data=data)


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

@bp.route('/page_1', methods=['GET', 'POST'])
def page_1():
    return render_template('Page-1.html')