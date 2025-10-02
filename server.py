import json
from flask import Flask,render_template,request,redirect,flash,url_for
from utils import check_competition_date, get_purchased_places
from data import save_clubs, save_competitions, load_clubs, load_competitions, save_booking
from datetime import datetime

from utils import filters_bp


app = Flask(__name__)
app.secret_key = 'something_special'
app.register_blueprint(filters_bp)

def reload_data():
    global competitions, clubs, booking_list
    competitions = load_competitions()
    clubs = load_clubs()
    
reload_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/welcome/<club_name>')
def welcome(club_name):
    club = next ((club for club in clubs if club['name'] == club_name), None)
    if not club:
        flash('unknown club')
        return redirect(url_for('index'))
    return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/show_summary',methods=['POST'])
def show_summary():
    club = next ((club for club in clubs if club['email'] == request.form['email']), None)
    if not club :
        return redirect(url_for("index"))
    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    found_club = next ((c for c in clubs if c['name'] == club), None)
    found_competition = next ((c for c in competitions if c['name'] == competition), None)
    if found_club and found_competition:
        available_places = 12 - get_purchased_places(club,competition)
        return render_template('booking.html',club=found_club,competition=found_competition,available_places=available_places)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchase_places',methods=['POST'])
def purchase_places():
    competition = next((c for c in competitions if c['name'] == request.form['competition']), None)
    club = next((c for c in clubs if c['name'] == request.form['club']), None)

    places_required = int(request.form['places'])
    places_number = int(competition['numberOfPlaces'])

    if places_required > 12 or places_required <= 0 :
        flash("Unauthorized purchase.")
        return redirect(url_for('welcome', club_name=club["name"]))
    
    if places_number < places_required :
        flash (f"They aren't available space for {places_required} places")
        return redirect(url_for('welcome', club_name=club["name"]))
    
    if int(club["points"]) < places_required:
        flash (f"You don't have enough points for purchase {places_required} places")
        return redirect(url_for('welcome', club_name=club["name"]))
    
    if not (check_competition_date(competition['date'])):
        flash ("The competition is over.")
        return redirect(url_for('welcome', club_name=club["name"]))
    
    places_purchased = get_purchased_places(club,competition)

    if ( places_purchased + places_required ) > 12:
        flash ("You have reached the purchase limit.")
        return redirect(url_for('welcome', club_name=club["name"]))
    
    club['points'] = str(int(club['points']) - places_required)
    competition['numberOfPlaces'] = str(places_number - places_required)
    booking={   "competition": competition['name'],
                "club": club['name'],
                "places": str(places_required),
                "reserved_at": str(datetime.now())}

  
    save_clubs(clubs)
    save_competitions(competitions)
    save_booking(booking)
    flash(f"Great-booking complete! You purcharsed {places_required} places.")
    return redirect(url_for('welcome', club_name=club["name"]))

    

# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))