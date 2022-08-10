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
def draw(window, paddles, ball):
    window.fill('black')

    for paddle in paddles:
        paddle.draw(window)
    
    for i in range(10, HEIGHT, HEIGHT//20): # To draw the dotted line
        if i % 2 == 0:
            pygame.draw.rect(window, 'white', (WIDTH//2 - 5, i, 10, HEIGHT // 20))

    ball.draw(window)
    pygame.display.update()

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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()
    handle_movement(keys, left_paddle, right_paddle)
    ball.move()

    draw(SCREEN, [left_paddle, right_paddle], ball)
    clock.tick(FPS)

