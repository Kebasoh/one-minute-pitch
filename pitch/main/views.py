from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/profile')
def profile():

	return render_template('profile.html')


@main.route('/pitches')
def pitches():
	return render_template('pitches.html')