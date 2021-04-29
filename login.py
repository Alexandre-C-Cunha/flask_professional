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

	if form.validate_on_submit():
		print("validando os dados")
		print(form.user.data)
		print(form.password.data)
		if form.user.data != 'Portuga_D_Ace':
			flash("Nome de Usuário não encontrado")
		elif form.password.data !='123roger':
			flash("Senha incorreta")
		else:
			flash("Obrigado por efetuar o login")
	return render_template('login.html', form=form)



if __name__=='__main__':
    app.run(debug=True)