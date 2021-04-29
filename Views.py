'''Flask Aplicativo Template
Licence: GPL3'''

from flask import url_for, redirect, render_template, Response, Flask, abort
from json import dumps
import locale


locale.setlocale( locale.LC_ALL, '' )
#Inciando uma aplicação simples
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!3'

# render template trás o html através do jinja

@app.route('/pag')
def index():
	return render_template('home.html')

#retorna uma string
@app.route('/string')
def retorna_string():
	return ("Isso é uma string")

#retorna um texto (com response e não é um html!)
@app.route('/text')
def text():
	return Response('escrevo uma string', status=200, mimetype='text/plain')

#retorna um objeto Json (aqui um dicionário)
@app.route('/json')
def json():

		d={
		'nome':'Luffy',
		'sobrenome':'Monkey D.',
		'Profissao':'Rei dos Piratas',
		'Idade':20}

		return Response(dumps(d), status=200, mimetype='application/json')

#url amigavel digitada na barra de tarefa

@app.route('/post/<slug>/')
def post(slug):
	return('Retornando o post: '+slug)

#testando com paramentros

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1,num2):
	try:
		if num2==0:
			resposta='A variavel digitada é zero!'
		else:
			resposta=num1*num2
	except:
		resposta='Valor digitado não é numero!'

	return str(resposta)

#usando paramentro 404 para quando algo der errado na pagina.

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return ('Poxa sinto muito Algo errado aconteceu! :('), 404


#usando abort

@app.route('/aborta/<int:num1>/<int:num2>')
def soma2(num1,num2):

	if num1 is not None and num2 is not None:
		
		return str(num1+num2)

	else:
		return abort(404)

#usando o redirect e usando o url for para redirecionar para a url específica
@app.route('/manda')
def manda():

	return redirect( url_for('json'))

if __name__=='__main__':
    app.run(debug=True)