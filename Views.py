'''Flask Aplicativo Template
Licence: GPL3'''



from flask import url_for, redirect, render_template, Response, Flask
from json import dumps
import locale


locale.setlocale( locale.LC_ALL, '' )
#Inciando uma aplicação simples
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!2'

if __name__=='__main__':
    app.run(debug=True)