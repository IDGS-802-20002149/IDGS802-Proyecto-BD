    
from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre')
    apellidos = StringField('apellidos')
    email = EmailField('correo')
    
class TeachForm(Form):
    id = IntegerField('id', [validators.DataRequired(message='Debes llenar todos los campos')])
    nombre = StringField('nombre', [validators.DataRequired(message='Debes llenar todos los campos')])
    apellidos = StringField('apellidos', [validators.DataRequired(message='Debes llenar todos los campos')])
    email = EmailField('correo', [validators.DataRequired(message='Debes llenar todos los campos')])