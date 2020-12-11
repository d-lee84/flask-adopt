"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf


class AddPetForm(FlaskForm):
    """ The pet add form accessed from the homepage """
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(),
                                      AnyOf(("cat",
                                             "dog",
                                             "porcupine"),
                                             message="""not a valid species, 
                                             please enter one of the following: 
                                             cat, dog, porcupine""")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField('Age',
                      choices=[
                               ('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')],
                      validators=[InputRequired()])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """ The pet edit form on the pet details page """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Is the pet available?")
