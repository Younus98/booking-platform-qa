import requests

BASE_URL = "https://automationintesting.online"


def test_room_list_is_available():
    response = requests.get(f"{BASE_URL}/api/room")

    assert response.status_code == 200
    rooms = response.json()["rooms"]
    assert len(rooms) > 0