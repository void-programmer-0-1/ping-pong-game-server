

class CanvasConfig:

    def __init__(self, width: int, height: int):
        self.screen_width: int = width
        self.screen_height: int = height     


class Paddle: # Player

    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.paddle_velocity_x: int = 0
        self.paddle_velocity_y: int = 0
        self.paddle_height: int = 0
        self.paddle_width: int = 0
        self.is_player_ai: bool = False

    def set_paddle_x(self, x: int):
        self.x = x

    def set_paddle_y(self, y: int):
        self.y = y

    def set_paddle_velocity_x(self, velocity_x: int):
        self.paddle_velocity_x = velocity_x

    def set_paddle_velocity_y(self, velocity_y: int):
        self.paddle_velocity_y = velocity_y

    def set_paddle_height(self, height: int):
        self.paddle_height = height

    def set_paddle_width(self, width: int):
        self.paddle_width = width

    def set_is_player_ai(self, is_ai: bool):
        self.is_player_ai = is_ai

    def move(self):
        pass

    def collision_with_ball(self, ball):
        pass


class Ball:

    def __init__(self):
        self.ball_radius: int = 0
        self.x: int = 0
        self.y: int = 0
        self.velocity_x: int = 0
        self.velocity_y: int = 0
    
    def set_ball_x(self, x: int):
        self.x = x
    
    def set_ball_y(self, y: int):
        self.y = y

    def set_ball_radius(self, r: int):
        self.ball_radius = r
    
    def set_ball_velocity_x(self, velocity_x: int):
        self.velocity_x = velocity_x
    
    def set_ball_velocity_y(self, velocity_y: int):
        self.velocity_y = velocity_y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
    
    def collision_detection(self, player1_paddle, player2_paddle):
        pass        
