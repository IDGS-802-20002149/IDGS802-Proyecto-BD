from flask import Flask, render_template, redirect
from flask import request, url_for
import forms
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route('/ABCompleto', methods=['GET','POST'])
def ABCompleto():
    form = forms.UserForm(request.form)
    alumno = Alumnos.query.all()
    
    return render_template('ABCompleto.html', form = form, alumno = alumno)

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(
            id = form.id.data,
            nombre = form.nombre.data,
            apellidos = form.apellidos.data,
            email = form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
        
    return render_template('Alumnos.html', form = form)

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        form.id.data = request.args.get('id')
        form.nombre.data = alum1.nombre
        form.apellidos.data = alum1.apellidos
        form.email.data = alum1.email
    
    if request.method == 'POST':
        id = form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = form.nombre.data
        alum.apellidos = form.apellidos.data
        alum.email = form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form=form)

@app.route('/eliminar', methods=['GET','POST'])
def eliminar():
    form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        form.id.data = request.args.get('id')
        form.nombre.data = alum1.nombre
        form.apellidos.data = alum1.apellidos
        form.email.data = alum1.email

    if request.method == 'POST':
        id = form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.nombre = form.nombre.data
        alum.apellidos = form.apellidos.data
        alum.email = form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
        
    return render_template('eliminar.html', form = form)
        
if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000)