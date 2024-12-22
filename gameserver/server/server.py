from fastapi import (
    FastAPI, Request, 
    HTTPException, status
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from models import (
    RoomCreationReq, 
    JoinRoomReq,
    generate_exception_message
)


from room import Room

rooms: list[Room] = []
room_index: dict[str, int] = {}

server = FastAPI()
server.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost:8000",  
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@server.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    error_details = [
        {"message": err["msg"]}
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"status": "error", "errors": error_details},
    )


@server.get("/")
async def home_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@server.get("/about")
async def about_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )


@server.get("/room")
async def room_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="room.html"
    )


@server.get("/game")
async def game_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="game.html"
    )


@server.post("/create-room")
async def create_room_route(request: RoomCreationReq):
    try:
        player1_name = request.player1
        player2_name = request.player2
        room = Room()
        room_code = room.create_room(player1_id=player1_name, player2_id=player2_name)
        room_number = len(rooms)
        rooms.append(room)
        room_index.update({str(room_code) : room_number})
        return {"status_code": 200, "message": "room created successfully", "room_code": room_code}

    except ValidationError as validation_error:
        error_message = generate_exception_message(
            error_count=validation_error.error_count(),
            error_list=validation_error.errors()
        )
        return HTTPException(status_code=422, detail=error_message)

    except Exception as error:
        print(f"Error occured in create_room_route :: {error}")
        raise HTTPException(status_code=500, detail="Internal server error")



@server.post("/join-room")
async def join_room(request: JoinRoomReq):
    try:
        room_code = request.room_code
        is_player_1 = request.is_player_1
        room_number: int = room_index[room_code]
        room = rooms[room_number]
        player1 = room.players[0]
        player2 = room.players[1]

        if is_player_1:
            # TODO assign paddle to the right
            player1.is_player_active = True
            print(player1.player_id)
        else:
            # TODO assign paddle to the right
            player2.is_player_active = True
            print(player2.player_id)

        # TODO redirect the user to the /game page on the success response
        return {"status_code": 200, "message": "joined room"}
    
    except ValidationError as validation_error:
        error_message = generate_exception_message(
            error_count=validation_error.error_count(),
            error_list=validation_error.errors()
        )
        return HTTPException(status_code=422, detail=error_message)

    except Exception as error:
        print(f"Error occured in join_room :: {error}")
        raise HTTPException(status_code=500, detail="Internal server error")
        
