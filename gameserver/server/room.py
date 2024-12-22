import uuid
from player import Player

class Room:

    def __init__(self):
        self.room_id: uuid.UUID = None
        self.players: list[Player] = []
        self.ideal_time_minute = 1

    def create_room(self, player1_id: str, player2_id: str) -> uuid.uuid4:
       
        # create the room unique id
        self.room_id = uuid.uuid4() 

        # add players to the room
        player1 = Player(player_id=player1_id, is_player_active=False)
        player2 = Player(player_id=player2_id, is_player_active=False)
        self.players.append(player1)
        self.players.append(player2)

        return self.room_id