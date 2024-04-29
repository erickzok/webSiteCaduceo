from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange

class ActividadForm(FlaskForm):
    proyecto = StringField('Proyecto', validators=[DataRequired(), Length(max=100)])
    JefeInmediato = StringField('Jefe Inmediato', validators=[DataRequired(), Length(max=50)])
    actividad = StringField('Actividad', validators=[DataRequired(), Length(max=100)])
    
    Porcentaje = IntegerField('Porcentaje de Avance', validators=[DataRequired(), NumberRange(min=0, max=100)])
    FechaFin = DateField('Fecha de Finalización', validators=[DataRequired()])
    comentarios = TextAreaField('Comentarios', validators=[DataRequired(), Length(max=100)])
