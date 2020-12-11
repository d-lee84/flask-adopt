"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(),
                                      AnyOf("cat",
                                            "dog",
                                            "porcupine",
                                            message="not a valid species")])
    photo_url = StringField("Photo URL", validators=[InputRequired(), URL()])
    age = SelectField('Age',
                      choices=[
                               ('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = StringField("Pet Name")
