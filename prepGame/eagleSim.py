import pygame
import spaceships
import shipAuxilliaries
import time
#
# General settings
# ================
screenWidth = 1200
screenHeight = 1000
physicalHeight = 1000 # in pysical dimensions --> m
#
dotsPerMeter = screenHeight/physicalHeight
#
isWaiting = 1
#
shipPolygonShape = [(0,10),(-10,-10),(10,-10)] # in pysical dimensions --> m

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
isRunning = True
dt = 0

tinyShip = spaceships.landingModuleA(0.5*screenWidth/dotsPerMeter, 0.9*screenHeight/dotsPerMeter, shipPolygonShape, dotsPerMeter)

while isRunning:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    #
    # Evaluation of player commands
    #
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        tinyShip.updateThrust(-1, 0.05)
    if keys[pygame.K_x]:
        tinyShip.updateThrust(-1, -0.05)
    if keys[pygame.K_s]:
        isWaiting = shipAuxilliaries.toogle(isWaiting)
        print('isWaiting:', isWaiting)
        time.sleep(0.2) 
    if keys[pygame.K_a]:
        tinyShip.shutOffThrust()
    #
    # Playground update procedure update procedure
    #
    if isWaiting == 0:
        tinyShip.updateMotion([0,-1], [0,0], dt)
    shipPolygon = tinyShip.placePolygon(screen.get_height())
    #
    #
    # Screen update procedure - identical for all scenarios
    #
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # Calculate and place the e´new positions of the polygon points on the screen.
    pygame.draw.polygon(screen, "white", shipPolygon)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()