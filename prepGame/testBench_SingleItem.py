import pygame
import shipClasses

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
isRunning = True
dt = 0

tinyShip = shipClasses.itemA(screen, [(10,10), (-10,10),(-10,-10),(10,-10)] )

while isRunning:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #
    tinyShip.updateCoordinatesAndAngle(dt)
    
    # pygame.draw.polygon(screen, "red", [(10,10), (-10,10),(-10,-10),(10,-10)]) 
    pygame.draw.polygon(screen, "white", tinyShip.placePolygon(screen.get_height()))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        tinyShip.updateVelocify(30 * dt)
    if keys[pygame.K_s]:
        tinyShip.updateVelocify((-30) * dt)
    if keys[pygame.K_a]:
        tinyShip.updateRotVelocity(1 * dt)
    if keys[pygame.K_d]:
        tinyShip.updateRotVelocity(-1 * dt)

    #print("v:",tinyShip.velocity," angle: ", tinyShip.angle, " x:", tinyShip.xCenter, " y:", tinyShip.yCenter, " dt:", dt)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()