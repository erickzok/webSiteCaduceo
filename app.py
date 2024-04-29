from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import config
from models.DAO.ActividadDAO import ActividadDAO
from models.ModelUser import ModelUser
from models.entities.Actividad import Actividad
from models.entities.ActividadForm import ActividadForm
from models.entities.User import User
from models.entities.UsuarioEmpleadoForm import UsuarioEmpleadoForm
from flask import redirect, url_for, flash

from models.entities.newUser import newUser


app = Flask(__name__)
app.config.from_object(config['development'])
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

csrf = CSRFProtect(app)
db = MySQL(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(0 , username, password,0)
        logged_user = ModelUser.login(db, user)
        if logged_user!=None:
            if logged_user.get_idRol()==2:
                print("Primer link")
                login_user(logged_user)
                return redirect(url_for('menu'))
                print(1)

            elif logged_user.get_idRol()==1:
                login_user(logged_user)
                return redirect(url_for('admin'))
                print(2)
            print("NINGUNO")
        else:
            flash("Usuario y/o contraseña inválida.")
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('login'))

@app.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

@app.route('/admin')
@login_required
def admin():
    actividad_dao = ActividadDAO(db, 0)
    actividades = actividad_dao.get_all_actividades()
    return render_template('adminTable/admin.html', actividades=actividades)
    

@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    form = UsuarioEmpleadoForm()
    error_message = None  # Inicializamos error_message como None
    
    if form.validate_on_submit():
        nombre = form.nombreEmpleado.data
        dni = form.DNI.data
        username = form.username.data
        password = form.password.data
        
        user = newUser(db, 0, username, password, dni, nombre)
        success, error_message = user.insertar_en_tablas()  # Cambiamos para obtener el mensaje de error desde insertar_en_tablas
        print(error_message)
        if success:
            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error al registrar usuario', 'error')
    
    return render_template('registrarUsuario.html', form=form, error_message=error_message)  # Pasamos error_message a la plantilla


@app.route('/home')
@login_required
def home():
    actividad_dao = ActividadDAO(db, current_user.idEmpleado)
    actividades = actividad_dao.get_all_actividades_for_id()
    return render_template('home.html', actividades=actividades)

@app.route('/registrarActividad', methods=['GET', 'POST'])
@login_required
def registrarActividad():
    form = ActividadForm()
    if form.validate_on_submit():
        now = datetime.now()
        hora_actual = now.strftime("%H:%M:%S")
        actividad = Actividad(
            db,
            proyecto=form.proyecto.data,
            JefeInmediato=form.JefeInmediato.data,
            actividad=form.actividad.data,
            Porcentaje=form.Porcentaje.data,
            FechaFin=form.FechaFin.data,
            hora=hora_actual,
            FechaRegistro=datetime.now(),
            comentarios=form.comentarios.data,
            idEmpleado=current_user.get_id()
        )
        actividad.insertar_actividad()
        flash('Actividad registrada exitosamente', 'success')
        return redirect(url_for('registrarActividad'))
    return render_template('registrarActividad.html', form=form)


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


