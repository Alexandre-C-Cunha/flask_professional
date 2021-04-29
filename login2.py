from flask import url_for, redirect, render_template, Response, Flask, abort, request, flash
from json import dumps
from forms import LoginForm
import locale
import os
SECRET_KEY = os.urandom(32)

locale.setlocale( locale.LC_ALL, '' )
#Inciando uma aplicação simples

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/login/', methods=['GET','POST'])
def login():
	form=LoginForm()
	error = None
	if form.validate_on_submit():
		print("validando os dados")
		print(form.user.data)
		print(form.password.data)
		if form.user.data != 'admin' or form.password.data != 'secret':
			error = 'Invalid credentials'
        	
		else:
			flash('You were successfully logged in')

	return render_template('login.html', form=form, error=error)



if __name__=='__main__':
    app.run(debug=True)