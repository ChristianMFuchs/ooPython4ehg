import pygame
import shipClasses

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
isRunning = True
dt = 0

tinyShipA = shipClasses.itemA(screen.get_width()/2, screen.get_height()/2, [(10,10), (-10,10),(-10,-10),(10,-10)] )
tinyShipB = shipClasses.itemA(screen.get_width()/4, screen.get_height()/2, [(10,10), (-10,10),(-10,-10),(10,-10)] )


while isRunning:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #
    tinyShipA.updateCoordinatesAndAngle(dt)
    tinyShipB.updateCoordinatesAndAngle(dt)

    # pygame.draw.polygon(screen, "red", [(10,10), (-10,10),(-10,-10),(10,-10)]) 
    #thePolygon = tinyShipA.placePolygon(screen.get_height())
    #nextPolygon = tinyShipB.placePolygon(screen.get_height())
    #for j in nextPolygon:
    #    thePolygon.append(j)

    pygame.draw.polygon(screen, "white", tinyShipA.placePolygon(screen.get_height()))
    pygame.draw.polygon(screen, "red", tinyShipB.placePolygon(screen.get_height()))

    # pygame.draw.polygon(screen, "white", thePolygon)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        tinyShipA.updateVelocify(30 * dt)
    if keys[pygame.K_s]:
        tinyShipA.updateVelocify((-30) * dt)
    if keys[pygame.K_a]:
        tinyShipA.updateRotVelocity(1 * dt)
    if keys[pygame.K_d]:
        tinyShipA.updateRotVelocity(-1 * dt)

    #print("v:",tinyShip.velocity," angle: ", tinyShip.angle, " x:", tinyShip.xCenter, " y:", tinyShip.yCenter, " dt:", dt)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()