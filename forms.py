from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form to create a new pet"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField('Photo URL of Pet', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(0,30, 'Invalid Age: please enter age between 0  and 30')])
    notes = TextAreaField('Notes', validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form to edit an exisiting pet"""

    photo_url = StringField('Photo of Pet', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Availablity')