# Remember PEP 8 Format
import pygame
import os
from sys import exit

os.system('clear')
pygame.init()

class Paddle: 
    VEL = 4 

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, window):
        pygame.draw.rect(window, 'white', (self.x, self.y, self.width, self.height))
    
    def move(self, up = True): 
        if up and self.y >= 0: # To prevent it from going off screen (top)
            self.y -= self.VEL
        elif not up and self.y <= (HEIGHT - self.height): # To prevent it from going off screen (bottom)
            self.y += self.VEL

class Ball:
    # Max Velocity for ball movement
    # It will start with the right paddle
    MAX_VEL = 5 

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self, window):
        pygame.draw.circle(window, 'white', (self.x, self.y), self.radius)
    
    def move(self): # We'll account for the velocity's signs (+ or -) in a different function
        self.x += self.x_vel
        self.y += self.y_vel

# Set up
WIDTH, HEIGHT = 700, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')
left_score = 0
right_score = 0
text_font = pygame.font.Font('/Users/username/Documents/Python_Files/Python Lessons and notes/Pygame Tutorial/font for tutorial/Pixeltype.ttf', 50)
FPS = 60
clock = pygame.time.Clock()


# For ball
RADIUS = 7
# Obvious for which
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100 

# Assign the classes to initiate
left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = Paddle(((WIDTH - 10) - PADDLE_WIDTH), HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = Ball(WIDTH//2, HEIGHT//2, RADIUS)


# To implement the classes onto the screen and constantly update
def draw(window, paddles, ball, left_score, right_score):
    window.fill('black')

    # To draw the paddles
    for paddle in paddles:
        paddle.draw(window)
    
    # Dash line in the middle
    for i in range(10, HEIGHT, HEIGHT//20): 
        if i % 2 == 0:
            pygame.draw.rect(window, 'white', (WIDTH//2 - 5, i, 10, HEIGHT // 20))

    # Scoreboard
                                                                                # We divide the game board into 4 quarters for proper score placement    
    r_score = text_font.render(f'Score: {right_score}', False, 'white')
    r_rect = r_score.get_rect(center = (WIDTH * (0.25), 100))                   # The R Score will be in the first quarter
    l_score = text_font.render(f'Score: {left_score}', False, 'white')
    l_rect = l_score.get_rect(center = (WIDTH * (0.75), 100))                   # The L score will be in the third
                                                                                # Second quarter is at mid and the Fourth will be WIDTH
    SCREEN.blit(r_score, r_rect)
    SCREEN.blit(l_score, l_rect)
    
    # Draws the ball
    ball.draw(window)

# For player(s)' input
def handle_movement(keys, left, right):
    if keys[pygame.K_w]:
        left.move(up = True)
    if keys[pygame.K_s]:
        left.move(up = False)
    
    if keys[pygame.K_UP]:
        right.move(up = True)
    if keys[pygame.K_DOWN]:
        right.move(up = False)


def handle_collision(ball, left, right):
    # The following will be for the collision of the ceiling
    if (ball.y + ball.radius) >= HEIGHT or (ball.y - ball.radius) <= 0:  # If just ball.y, it'll point at the center. Must get outer part of ball by adding or subtracting the radius, depending on the position
        ball.y_vel *= -1 # Reverse the velocity

    # Check the direction of the ball
    # If x's velocity is negative, it'll be going to the left paddle
    if ball.x_vel < 0:
        if ball.y >= left.y and ball.y <= left.y + left.height:
            if ball.x - ball.radius <= left.x + left.width:
                ball.x_vel *= -1

                # In order to prevent a boring game, we must implement different types of 'physics'
                # Hitting the center of the paddle will yield 0 y velocity
                # While hitting further away from the center will yield an ever so increasing angle
                middle_y_axis = left.y + left.height / 2
                difference_in_y = middle_y_axis - ball.y
                reduction_factor = (left.height/2) / ball.MAX_VEL
                y_vel = difference_in_y /reduction_factor
                ball.y_vel = -y_vel

    # Otherwise, it would go to the right
    else:
        if ball.y >= right.y and ball.y <= right.y + right.height:
            if ball.x + ball.radius >= right.x:
                ball.x_vel *= -1

                middle_y_axis = right.y + right.height / 2
                difference_in_y = middle_y_axis - ball.y
                reduction_factor = (right.height/2) / ball.MAX_VEL
                y_vel = difference_in_y /reduction_factor
                ball.y_vel = -y_vel

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    handle_movement(keys, left_paddle, right_paddle)
    handle_collision(ball, left_paddle, right_paddle)
    ball.move()
    
    if ball.x < 0:
        right_score += 1
    elif ball.x > WIDTH:
        left_score += 1
        

    draw(SCREEN, [left_paddle, right_paddle], ball, left_score, right_score)
    pygame.display.update()
    clock.tick(FPS)
