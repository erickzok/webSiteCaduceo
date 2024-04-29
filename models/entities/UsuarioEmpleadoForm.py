from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class UsuarioEmpleadoForm(FlaskForm):
    nombreEmpleado = StringField('Nombre del Empleado', validators=[DataRequired(), Length(max=100)])
    DNI = StringField('DNI', validators=[DataRequired(), Length(max=50)])
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=50)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), Length(min=8, max=50)])
