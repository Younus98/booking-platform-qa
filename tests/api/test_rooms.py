import pytest

from cerberus import Validator

ROOM_SCHEMA = {
    "roomid": {"type": "integer", "required": True},
    "roomName": {"type": "string", "required": True},
    "type": {"type": "string", "required": True},
    "roomPrice": {"type": "integer", "required": True},
    "accessible": {"type": "boolean", "required": True},
    "features": {"type": "list", "schema": {"type": "string"}},
    "description": {"type": "string"},
    "image": {"type": "string"},
}


def get_rooms(api, base_url):
    response = api.get(f"{base_url}/api/room")
    assert response.status_code == 200
    return response.json()["rooms"]


def test_room_list_returns_json(api, base_url):
    response = api.get(f"{base_url}/api/room")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    assert response.json()["rooms"]


def test_every_room_matches_schema(api, base_url):
    validator = Validator(ROOM_SCHEMA, allow_unknown=True)

    for room in get_rooms(api, base_url):
        assert validator.validate(room), f"Room {room.get('roomid')}: {validator.errors}"


def test_room_prices_are_positive(api, base_url):
    for room in get_rooms(api, base_url):
        assert room["roomPrice"] > 0, f"Room {room['roomName']} has price {room['roomPrice']}"


def test_room_ids_are_unique(api, base_url):
    ids = [room["roomid"] for room in get_rooms(api, base_url)]

    assert len(ids) == len(set(ids)), f"Duplicate room ids: {ids}"


ALLOWED_ROOM_TYPES = ["Single", "Double", "Twin", "Family", "Suite"]


def test_room_types_are_valid(api, base_url):
    for room in get_rooms(api, base_url):
        assert room["type"] in ALLOWED_ROOM_TYPES, f"Room {room['roomName']} has invalid type {room['type']}"


def test_every_room_has_features(api, base_url):
    for room in get_rooms(api, base_url):
        assert len(room["features"]) > 0, f"Room {room['roomName']} has no features"


@pytest.mark.xfail(reason="Known defect: /api/room/{id} returns a server error, see docs/defects.md")
def test_single_room_can_be_fetched(api, base_url):
    response = api.get(f"{base_url}/api/room/1")

    assert response.status_code == 200
    assert response.json()["roomid"] == 1


@pytest.mark.xfail(reason="Known defect: invalid room IDs return 500 instead of 404")
@pytest.mark.parametrize("room_id", ["not-a-room", "999999"])
def test_invalid_room_id_returns_not_found(api, base_url, room_id):
    response = api.get(f"{base_url}/api/room/{room_id}")

    assert response.status_code == 404