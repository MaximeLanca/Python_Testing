import pytest
from unittest.mock import patch
import json
import server
import data



# @pytest.fixture(autouse=True)
# def patch_reload(monkeypatch):
#     def fake_reload():
#         server.clubs = data.load_clubs()
#         server.competitions = data.load_competitions()
#     monkeypatch.setattr(server, "reload_data", fake_reload, raising=True)

@pytest.fixture
def app():
    """Fixture requise par pytest-flask : retourne l'app Flask."""
    server.app.config.update(TESTING=True, SECRET_KEY="test")
    return server.app


@pytest.fixture
def client():
    return server.app.test_client()

    
@pytest.fixture(autouse=True)
def patch_load_save(bookings_path):

    def fake_load_booking(path="bookings.json"):
        return json.loads(bookings_path.read_text(encoding="utf-8")).get("bookings", [])

    def fake_save_booking(booking, path="bookings.json"):
        bookings = fake_load_booking()
        bookings.append(booking)
        bookings_path.write_text(json.dumps({"bookings": bookings}, indent=2), encoding="utf-8")


    with patch("utils.load_booking", side_effect=fake_load_booking), \
    patch("data.load_booking", side_effect=fake_load_booking), \
    patch("server.save_booking", side_effect=fake_save_booking), \
    patch("server.save_clubs", lambda *a, **k: None), \
    patch("server.save_competitions", lambda *a, **k: None):
        
        yield
    
@pytest.fixture
def bookings_path (tmp_path):

    bookings_path = tmp_path / "bookings_test.json"
    bookings_path.write_text('{"bookings": []}', encoding="utf-8")

    return bookings_path