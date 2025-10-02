
def test_unknown_club_redirect(client):
    response = client.get("welcome/fake_club", follow_redirects=True)
    assert response.status_code == 200