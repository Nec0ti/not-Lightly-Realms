import pygame
import sys

# Initialize the game
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mystic Realms")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

# Player settings
player_radius = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Portal settings
portal_radius = 30
portal_position = None
current_realm = 1
realms = {
    1: "Realm 1",
    2: "Realm 2",
    3: "Realm 3"
}

# Level design settings
levels = {
    1: [
        {"position": (100, 100), "color": GRAY},
        {"position": (300, 300), "color": GRAY},
        {"position": (500, 500), "color": GRAY}
    ],
    2: [
        {"position": (200, 200), "color": GRAY},
        {"position": (400, 400), "color": GRAY},
        {"position": (600, 600), "color": GRAY}
    ],
    3: [
        {"position": (150, 150), "color": GRAY},
        {"position": (350, 350), "color": GRAY},
        {"position": (550, 550), "color": GRAY}
    ]
}

current_level = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Create a portal when the left mouse button is pressed
    if pygame.mouse.get_pressed()[0]:
        portal_position = pygame.mouse.get_pos()

    # Check the distance between the portal and the player
    if portal_position:
        distance_to_portal = pygame.math.Vector2(player_x - portal_position[0], player_y - portal_position[1]).length()

        # Change the realm if the distance between the portal and the player is below a certain threshold
        if distance_to_portal < portal_radius:
            current_realm = (current_realm % 3) + 1  # Loop between 1, 2, 3

            # Additionally, reset the portal position
            portal_position = None

            # Change the level every three realms
            if current_realm % 3 == 0:
                current_level = (current_level % 3) + 1

    # Clear the game screen
    screen.fill(BLACK)

    # Draw the player character
    pygame.draw.circle(screen, LIGHT_BLUE, (int(player_x), int(player_y)), player_radius)

    # Draw the portal
    if portal_position:
        pygame.draw.circle(screen, RED, portal_position, portal_radius)

    # Draw the current level design
    for obstacle in levels[current_level]:
        obstacle_rect = pygame.Rect(obstacle["position"][0], obstacle["position"][1], 30, 30)
        pygame.draw.rect(screen, obstacle["color"], obstacle_rect)

        # Check for collision with player
        if obstacle_rect.collidepoint(player_x, player_y):
            if keys[pygame.K_SPACE]:
                obstacle["position"] = pygame.mouse.get_pos()

    # Update the screen
    pygame.display.flip()

    # FPS control
    pygame.time.Clock().tick(60)
