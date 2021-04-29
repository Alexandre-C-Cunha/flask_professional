from flask import url_for, redirect, render_template, Response, Flask, abort, request, flash, send_from_directory
from json import dumps
from forms import LoginForm
from flask_caching import Cache
import locale
import os
from werkzeug.utils import secure_filename
SECRET_KEY = os.urandom(32)


locale.setlocale( locale.LC_ALL, '' )
#Inciando uma aplicação simples

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
UPLOAD_ARQUIVOS='tmp/upload'
TIPOS_EXTENSÕES=set(['txt','pdf','png','jpg','jpeg','gif'])
app.config['UPLOAD_ARQUIVOS']=UPLOAD_ARQUIVOS
app.config['CACHE_TYPE']='simple'

cache=Cache(app)

def arquivo_permitido(filename):
	return('.' in filename and filename.rsplit('.',1)[1].lower() in TIPOS_EXTENSÕES)

@app.route('/upload/', methods=['GET','POST'])
def upload():
	if request.method=='POST':
		file=request.files['file']
		if file and arquivo_permitido(file.filename):
			filename= secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_ARQUIVOS'], filename))
			flash('Arquivos enviados com sucesso')

			return render_template('upload.html', filename=filename)
	else:
		return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_ARQUIVOS'],filename)



if __name__=='__main__':
    app.run(debug=True)