rooms = [
    {"roomName": "101", "type": "Single", "roomPrice": 100},
    {"roomName": "102", "type": "Double", "roomPrice": 150},
    {"roomName": "103", "type": "Suite", "roomPrice": 225},
]

for room in rooms:
    print(f"Room {room['roomName']} has price €{room['roomPrice']}")