"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf, Length

AGE_CHOICE = [('baby', 'Baby'),
              ('young', 'Young'),
              ('adult', 'Adult'),
              ('senior', 'Senior')]
SPECIES = ("cat", "dog", "porcupine")
SPECIES_CHOICE = [(species, species.capitalize()) for species in SPECIES]


class AddPetForm(FlaskForm):
    """ The pet add form accessed from the homepage """
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species",
                          choices=SPECIES_CHOICE,
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField('Age',
                      choices=AGE_CHOICE,
                      validators=[InputRequired()])
    notes = StringField("Notes", validators=[Optional(),
                                             Length(min=5,
                                                    max=200,
                                                    message="please enter 5-200 charactors")])


class EditPetForm(FlaskForm):
    """ The pet edit form on the pet details page """

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional(),
                                             Length(min=5,
                                                    max=200,
                                                    message="please enter 5-200 charactors")])
    available = BooleanField("Is the pet available?")
