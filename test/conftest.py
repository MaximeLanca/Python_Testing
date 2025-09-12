import pytest
import server
from copy import deepcopy

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


@pytest.fixture(params=[
    [{"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "25"}],
])
def competition_line_up_twenty_five_places(request,monkeypatch):
    monkeypatch.setattr(server,"competitions",deepcopy(request.param))
    return server.competitions

@pytest.fixture(params=[
    [{"name": "Spring Festival", "date": "2027-10-10 09:00:00", "numberOfPlaces": "10"}],
])
def competition_line_up_ten_places(request,monkeypatch):
    monkeypatch.setattr(server,"competitions",deepcopy(request.param))
    return server.competitions

@pytest.fixture(params=[
    [{"name": "Spring Festival", "date": "2025-08-10 09:00:00", "numberOfPlaces": "10"}],
])
def finished_competition(request,monkeypatch):
    monkeypatch.setattr(server,"competitions",deepcopy(request.param))
    return server.competitions

@pytest.fixture(params=[
    [{"name":"Simply Lift", "email":"john@simplylift.co", "points":"10"}]
])
def club_with_ten_points(request, monkeypatch):
    monkeypatch.setattr(server,"clubs",deepcopy(request.param))
    return server.clubs

@pytest.fixture
def clubs_simply_lift(monkeypatch):
    monkeypatch.setattr(
        server, "clubs",
        [{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"}]
    )

@pytest.fixture(autouse=True)
def no_backup(monkeypatch):
    monkeypatch.setattr("server.save_clubs", lambda clubs, path="clubs.json": None, raising=True)
    monkeypatch.setattr("server.save_competitions", lambda competitions, path="competitions.json": None, raising=True)
