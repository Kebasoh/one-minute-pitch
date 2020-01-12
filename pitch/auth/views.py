from flask import render_template
from . import auth
from .forms import RegisterUserForm,LoginUserForm

@auth.route('/registerUser')
def registerUser():
	registration_form = RegisterUserForm()
	return render_template('auth/register.html', registration_form = registration_form)


@auth.route('/login')
def login():
	login_form = LoginUserForm()
	return render_template('auth/login.html', login_form = login_form)