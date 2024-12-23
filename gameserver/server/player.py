from game import (
    Paddle, CanvasConfig
)

class Player:

    def __init__(self, player_id: str, is_player_active: bool):
        self.player_id: str = player_id
        self.player_paddle: Paddle = None
        self.score: int = 0
        self.is_winner: bool = False
        self.is_player_active: bool = is_player_active
    
    def set_paddles(self,canvas_config: CanvasConfig, side: str):
        if side == "left":
            self.player_paddle.set_paddle_height(100)
            self.player_paddle.set_paddle_width(15)
            self.player_paddle.set_paddle_x(15)
            self.player_paddle.set_paddle_y(canvas_config.screen_height / 2 - self.player_paddle.paddle_height / 2)
            self.player_paddle.set_paddle_velocity_x(5)
            self.player_paddle.is_player_ai(False)

        else:
            ...

    def update_player_paddle(self):
        pass

    def score_up(self):
        pass