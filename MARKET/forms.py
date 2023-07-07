from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Contact(FlaskForm):
    Nom = StringField("Nom", validators=[DataRequired()])
    Prenom = StringField("Prenoms", validators=[DataRequired()])
    Email = StringField("Email", validators=[DataRequired()])
    Message = TextAreaField("Message", validators=[DataRequired()])    # dark_Mode = SubmitField("Pass into Dark Mode")
    submit = SubmitField("Submit")
