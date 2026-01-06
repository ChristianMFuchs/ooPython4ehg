import pygame, random, bomberClasses, numpy  

def main():

    # Define some colors
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    # Initialize Pygame
    pygame.init()
    
    # Set the height and width of the screen
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])
    
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    # block_list = pygame.sprite.Group()
    
    # This is a list of every sprite. All blocks and the player block as well.
    all_dynamic_sprites_list = pygame.sprite.Group()
    all_bombs_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    
    myBomber = bomberClasses.bomber(screen, RED, 10, 10)
    all_sprites_list.add(myBomber)
    all_dynamic_sprites_list.add(myBomber)
    all_sprites_list.add(myBomber)
    #
    myBottom = bomberClasses.generalRectangle(screen, BLACK, 690, 5, 5, 390)
    all_sprites_list.add(myBottom)

    myTarget = bomberClasses.generalRectangle(screen, BLACK, 50,25,350,370)
    all_sprites_list.add(myTarget)

    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        #
        # Evaluate Mouse commands
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
        # Clear the screen
        screen.fill(WHITE)

        # Check for request to throw bomb
        if myBomber.attackState == "LAUNCH_THROW":
            myBomber.attackState = "LAUNCH_THROW_DONE"
            newStupidBomb = bomberClasses.stupidBomb(screen, myBomber, BLACK, 3, 5)
            all_bombs_list.add(newStupidBomb)
            all_dynamic_sprites_list.add(newStupidBomb)
            all_sprites_list.add(newStupidBomb)
        #
        # Check for collisions between bombs and ground --> remove bombs if needed
        #
        bombs_hits_gound_list = pygame.sprite.spritecollide(myBottom, all_bombs_list, True)
        print(len(all_bombs_list), len(bombs_hits_gound_list))
    
        # Check for collisions between bombs and target --> remove bombs if needed
        #
        bombs_hits_target_list = pygame.sprite.spritecollide(myTarget, all_bombs_list, True)
        if len(bombs_hits_target_list)> 0:
            print("Hit .... .")
            # all_sprites_list.remove(myTarget)
            myTarget.rect.y = 0
            myTarget.kill()

        #
        # All evaluation should be done before. Now update of dynamic sprites and drawing happens
        # as end of the sequence.
        #
        # Update all sprites that can change within the game. 
        all_dynamic_sprites_list.update()
        # Draw all the spites
        all_sprites_list.draw(screen)
        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    pygame.quit()

main()