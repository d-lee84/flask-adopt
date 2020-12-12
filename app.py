"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

from pet_finder import get_random_pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def show_pets():
    """ Shows the homepage and listing of the pets """
    pets = Pet.query.all()
    random_pet = get_random_pet()
    return render_template('homepage.html', pets=pets, random_pet=random_pet)


@app.route('/add', methods=["GET","POST"])
def add_pet():
    """ handle add pet form"""

    form = AddPetForm()
    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data   

        pet = Pet()
        form.populate_obj(pet)
        db.session.add(pet)
        db.session.commit()
        flash("Created successfully")
        return redirect("/")
    else: 
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def handle_pet_listing_and_edit_form(pet_id):
    """ Handle showing pet information and edit form """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()

        flash("The edit has been submitted!")

        return redirect(f"/{pet.id}")
    else:
        return render_template("pet_details.html", form=form, pet=pet)

