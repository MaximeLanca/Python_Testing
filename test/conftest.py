import pytest
import server
import data

@pytest.fixture
def app():
    """Fixture requise par pytest-flask : retourne l'app Flask."""
    server.app.config.update(TESTING=True, SECRET_KEY="test")
    return server.app

@pytest.fixture
def client():
    return server.app.test_client()

@pytest.fixture
def user_context():
    data = {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
    }
    return data


@pytest.fixture
def competition_line_up_twenty_five_places(monkeypatch):
    monkeypatch.setattr(data,"load_competitions",[{"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "25"}])
    server.reload_data()
    return server.competitions

@pytest.fixture
def competition_line_up_ten_places(monkeypatch):
    monkeypatch.setattr(data,"load_competitions",[{"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "10"}])
    server.reload_data()
    return server.competitions

@pytest.fixture
def finished_competition(monkeypatch):
    monkeypatch.setattr(data,"load_competitions",[{"name": "Spring Festival", "date": "2025-08-10 09:00:00", "numberOfPlaces": "10"}])
    server.reload_data()
    return server.competitions

@pytest.fixture
def club_with_ten_points(monkeypatch):
    monkeypatch.setattr(data,"load_clubs",[{"name":"Simply Lift", "email":"john@simplylift.co", "points":"10"}])
    server.reload_data()
    return server.clubs

@pytest.fixture
def clubs_simply_lift(monkeypatch):
    monkeypatch.setattr(data, "load_clubs",[{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}])
    server.reload_data()
    return server.clubs

@pytest.fixture(autouse=True)
def no_backup(monkeypatch):
    monkeypatch.setattr("data.save_clubs", lambda clubs, path="clubs.json": None, raising=True)
    monkeypatch.setattr("data.save_competitions", lambda competitions, path="competitions.json": None, raising=True)
