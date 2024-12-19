from fastapi import (
    FastAPI, Request, Depends, 
    HTTPException, status
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from models import RoomCreationReq, generate_exception_message

server = FastAPI()
server.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


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
        return {"status_code": "200", "message": "room created successfully"}

    except ValidationError as validation_error:
        error_message = generate_exception_message(
            error_count=validation_error.error_count(),
            error_list=validation_error.errors()
        )
        return HTTPException(status_code=422, detail=error_message)

    except Exception as error:
        print(f"Error occured in create_room_route :: {error}")
        raise HTTPException(status_code=500, detail="Internal server error")


