from flask import url_for, redirect, render_template, Response, Flask, abort
from json import dumps
import locale


locale.setlocale( locale.LC_ALL, '' )
#Inciando uma aplicação simples
from flask import Flask
app = Flask(__name__)


# render template trás o html através do jinja

@app.route('/home')
def index():
	#é possivel incluir um variavél direto no projeto
	nome=12
	#incluir uma lista com controle de palavras chamada truncate ver no home2.html
	posts=[
			"Lorem ipsum ante consectetur sed semper quam inceptos, ultrices est viverra molestie dictum ultrices per, non iaculis habitant urna fames libero. class eget lectus sociosqu primis ligula sapien venenatis laoreet, condimentum dapibus ultrices sit elementum nisl odio nostra, turpis lacinia a cubilia auctor erat et. vivamus tortor ultricies interdum vivamus fusce lectus consequat torquent iaculis viverra vulputate nibh conubia himenaeos posuere, pulvinar morbi euismod tellus lectus magna mauris aenean netus morbi sit purus ac. etiam scelerisque aliquet tempus quisque amet netus litora, ante dictum viverra cubilia libero vitae iaculis, libero praesent curabitur ultricies aliquet taciti.",
			"Lorem ipsum ante consectetur sed semper quam inceptos, ultrices est viverra molestie dictum ultrices per, non iaculis habitant urna fames libero. class eget lectus sociosqu primis ligula sapien venenatis laoreet, condimentum dapibus ultrices sit elementum nisl odio nostra, turpis lacinia a cubilia auctor erat et. vivamus tortor ultricies interdum vivamus fusce lectus consequat torquent iaculis viverra vulputate nibh conubia himenaeos posuere, pulvinar morbi euismod tellus lectus magna mauris aenean netus morbi sit purus ac. etiam scelerisque aliquet tempus quisque amet netus litora, ante dictum viverra cubilia libero vitae iaculis, libero praesent curabitur ultricies aliquet taciti.",
			"Lorem ipsum ante consectetur sed semper quam inceptos, ultrices est viverra molestie dictum ultrices per, non iaculis habitant urna fames libero. class eget lectus sociosqu primis ligula sapien venenatis laoreet, condimentum dapibus ultrices sit elementum nisl odio nostra, turpis lacinia a cubilia auctor erat et. vivamus tortor ultricies interdum vivamus fusce lectus consequat torquent iaculis viverra vulputate nibh conubia himenaeos posuere, pulvinar morbi euismod tellus lectus magna mauris aenean netus morbi sit purus ac. etiam scelerisque aliquet tempus quisque amet netus litora, ante dictum viverra cubilia libero vitae iaculis, libero praesent curabitur ultricies aliquet taciti."
	]
	return render_template('home2.html', nome=nome, posts=posts)


if __name__=='__main__':
    app.run(debug=True)