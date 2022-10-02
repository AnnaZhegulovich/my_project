from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import Form


class MyForm(Form):
    pressure_sist = IntegerField(" АД систолическое: ", validators=[DataRequired(), Length(max=3)])
    pressure_dia = IntegerField("АД диастолическое: ", validators=[DataRequired(), Length(max=3)])
    breath = IntegerField("ЧДД: ", validators=[DataRequired(), Length(max=2)])
    pulse = IntegerField("ЧСС: ", validators=[DataRequired(), Length(max=3)])
    iss = IntegerField("Баллы ISS: ", validators=[DataRequired(), Length(max=3)])
    gsg = IntegerField("Баллы шкалы Глазго: ", validators=[DataRequired(), Length(max=2)])
    submit = SubmitField("Отправить данные")



