import pygame, os
from sys import exit

os.system('clear')


# class Ball:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y
#         self.circle = pygame.draw.circle(screen, 'white', (600, 400), 10)
# 
# 
#     def move(self):
#         self.x -= 2
#         self.y -= 2
#         if self.y >= 800 or self.y <= 0:
#             self.y *= -1
#     
#     def update(self):
#         
    
def change_direction(y_pos):
    if y_pos >= SCREEN_HEIGHT or y_pos <= 0:
        y_pos = y_pos * -1
    return y_pos
        
    

pygame.init()
clock = pygame.time.Clock()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x_pos, y_pos = 600, 400

game_active = True
# ball = pygame.sprite.GroupSingle
# ball.add(Ball())
x_pos, y_pos = 600, 400
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            y_pos -= 2

    if game_active:
        screen.fill('black')
        rect = pygame.draw.circle(screen, 'white', (x_pos, y_pos), 10)
        print(y_pos)
        y_pos = change_direction(y_pos)
       
       

        pygame.display.update()
        clock.tick(60)
