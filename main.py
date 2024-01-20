import pygame
import sys
import random
import pygame_gui

from pygame_gui.ui_manager import UIManager
from pygame_gui.elements.ui_text_box import UITextBox
from pygame_gui.core import IncrementalThreadedResourceLoader, ObjectID
from pygame_gui import UI_TEXT_BOX_LINK_CLICKED, UI_TEXT_EFFECT_FINISHED
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
levels = {
    0: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    1: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    2: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    3: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    4: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    5: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    },
    6: {
        "background_color": BLACK,
        "boxes": [pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40),
                  pygame.Rect(random.randint(0, 1550), random.randint(0, 850), 40, 40)]
    }
}

current_level = 0

# Text
font = pygame.font.Font('fonts/Pixel.TTF', 32)
text = font.render(f'Current Level: {current_level}', True, GOLD, BLUE)
textRect = text.get_rect()
textRect.center = (1600 // 2, 900 // 2)

level_text = font.render(f'Current Level: {current_level}', True, GOLD, BLUE)
level_text_rect = level_text.get_rect()
level_text_rect.center = (1600 // 2, 50)
screen.blit(level_text, level_text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(text, textRect)
    collide = pygame.Rect.colliderect(player_rect, levels[current_level]["boxes"][0])
    
    # When collides correct object scene count +1
    if collide:
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/object.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(1)
        current_level += 1

    screen.fill(levels[current_level]["background_color"])
    
    pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), light_radius)
    pygame.draw.rect(screen, LIGHT_BLUE, player_rect)
    
    for box in levels[current_level]["boxes"]:
        pygame.draw.rect(screen, BLACK, box)
          
    #pygame.draw.circle(screen, WHITE, (int(light_x), int(light_y)), light_radius)
    #pygame.draw.rect(screen, LIGHT_BLUE, player_rect)
    

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
    
    light_x = player_rect.x + 25
    light_y = player_rect.y + 25

    deltatime = clock.tick(60) / 1000
    
    if current_level >= len(levels):
        pass # Finish screen

pygame.quit()