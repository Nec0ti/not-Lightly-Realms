import pygame
import sys
from pygame.locals import *


# Initialize the game
pygame.init()

clock = pygame.time.Clock()

# Screen settings
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("! Lightly Realms")

# Colors
BLACK = (0, 0, 0)
GOLD = (77, 61, 0)
BLUE = (96, 97, 249)
BLOOD = (78, 4, 21)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

# Other rects
# Level 1
box_rect1 = pygame.Rect(800, 548, 40, 60)
box_rect2 = pygame.Rect(1400, 120, 40, 70)
box_rect3 = pygame.Rect(100, 847, 40, 40)

# Player settings
player_rect = pygame.Rect(775, 425, 50, 50)
player_speed = 300
deltatime = 0
# light
light_radius = 100
light_x, light_y = WIDTH // 2, HEIGHT // 2

# Levels
current_level = 0

levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(BLACK)

    pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), light_radius)
    pygame.draw.rect(screen, BLACK, box_rect1)
    pygame.draw.rect(screen, BLACK, box_rect2)
    pygame.draw.rect(screen, BLACK, box_rect3)
    pygame.draw.rect(screen, LIGHT_BLUE, player_rect)

    pygame.display.update()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= player_speed * deltatime
        light_y -= player_speed * deltatime
    if keys[pygame.K_s]:
        player_rect.y += player_speed * deltatime
        light_y += player_speed * deltatime
    if keys[pygame.K_a]:
        player_rect.x -= player_speed * deltatime
        light_x -= player_speed * deltatime
    if keys[pygame.K_d]:
        player_rect.x += player_speed * deltatime
        light_x += player_speed * deltatime
        
    pygame.display.flip()

    deltatime = clock.tick(60) / 1000

pygame.quit()