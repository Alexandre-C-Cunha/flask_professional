from flask import url_for, redirect, render_template, Response, Flask, abort
from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length
from json import dumps
import locale


class LoginForm(Form):
	user=TextField(u'Usuário', validators = [DataRequired()])
	password=PasswordField(u'Senha', validators=[Length(min=6)])