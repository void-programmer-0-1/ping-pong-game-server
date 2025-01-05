import uuid
from pydantic import BaseModel, field_validator

class RoomCreationReq(BaseModel):
    player1: str
    player2: str

    @field_validator("player1")
    def validate_player1_name(cls, player1: str) -> str:
        name_len = len(player1)
        if name_len <= 6:
            raise ValueError("Name should contain more than 6 charaters")
        return player1

    @field_validator("player2")
    def validate_player2_name(cls, player2: str) -> str:
        name_len = len(player2)
        if name_len <= 6:
            raise ValueError("Name should contain more than 6 characters")
        return player2


class JoinRoomReq(BaseModel):
    room_code: str
    is_room_creator: bool 

    @field_validator("room_code")
    def validate_room_code(cls, room_code: uuid.uuid4) -> uuid.uuid4:
        try:
            _ = uuid.UUID(room_code, version=4)
        except Exception as err:
            return ValueError("Invalid Room Code")
        return room_code


class GetRoomInfoReq(BaseModel):
    room_code: str

    @field_validator("room_code")
    def validate_room_code(cls, room_code: uuid.uuid4) -> uuid.uuid4:
        try:
            _ = uuid.UUID(room_code, version=4)
        except Exception as err:
            return ValueError("Invalid Room Code")
        return room_code


def generate_exception_message(error_count: int, error_list: list) -> str:
    error_string = ""
    for i in range(error_count):
        error_string += error_list[i]["msg"]
        error_string += "\n" if i + 1 != error_count else ""
    return error_string

