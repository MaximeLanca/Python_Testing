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

#@pytest.fixture(autouse=True)
#def reset_data (monkeypatch):
    # competitions = [{"name": "Spring Festival", "date": "2026-03-27 10:00:00", "numberOfPlaces": "25"},]
    #monkeypatch.setattr(server, "competitions", deepcopy(competitions), raising=True)


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

