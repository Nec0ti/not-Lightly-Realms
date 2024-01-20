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
#levels = {
#    0: [
#        {"position": (100, 100), "color": BLACK,},
#        {"position": (300, 300), "color": BLACK,},
#        {"position": (500, 500), "color": BLACK,}
#    ],
#    1: [
#        {"position": (100, 100), "color": BLACK,},
#        {"position": (300, 300), "color": BLACK,},
#        {"position": (500, 500), "color": BLACK,}
#    ],
#    2: [
#        {"position": (200, 200), "color": BLACK,},
#        {"position": (400, 400), "color": BLACK,},
#        {"position": (600, 600), "color": BLACK,}
#    ],
#    3: [
#        {"position": (150, 150), "color": BLACK,},
#        {"position": (542, 566), "color": BLACK,},
#        {"position": (550, 720), "color": BLACK,}
#    ]
#}

current_level = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
    collide = pygame.Rect.colliderect(player_rect, box_rect3)

    # When collides correct object scene count +1
    if collide:
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/object.wav")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1)
        current_level += 1
        
    screen.fill(BLACK)

    #pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), light_radius)
    #pygame.draw.rect(screen, LIGHT_BLUE, player_rect)
    
        
    if current_level == 0:
        pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), light_radius)
        pygame.draw.rect(screen, BLACK, box_rect1)
        pygame.draw.rect(screen, BLACK, box_rect2)
        pygame.draw.rect(screen, BLACK, box_rect3)
        pygame.draw.rect(screen, LIGHT_BLUE, player_rect)
        
    if current_level == 1:
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